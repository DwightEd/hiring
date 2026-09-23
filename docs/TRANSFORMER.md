# 手写 Transformer：从多头注意力到完整前向

从仓库根目录运行 `python transformer_demo.py`，或者在 VS Code 打开该入口并按 F5。
依赖只有 NumPy：`python -m pip install -r requirements.txt`。

实现采用 [Attention Is All You Need 第 3 节](https://arxiv.org/html/1706.03762v7#S3) 的
Encoder–Decoder、Post-LayerNorm、ReLU FFN 和正弦位置编码，展示推理模式的完整前向。
Dropout 在推理模式为恒等，因此没有随机丢弃步骤；未实现训练循环、整网反向传播、KV cache
或逐 token 生成。嵌入和输出投影不共享权重，多头注意力采用无偏置投影。
所有权重随机初始化，输出只能用于理解维度和数据流，没有翻译或语言能力。

## 入口、参数与文件职责

执行路径是 `main() -> Transformer(...).forward(source, target) -> logits -> softmax 展示概率`。
`forward` 返回未归一化的 logits，便于将来接交叉熵；演示在展示结果时才计算概率。

| 文件 / 入口 | 职责 |
|---|---|
| [transformer_demo.py](../transformer_demo.py) / `main()` | 解析命令行，构造模型，调用前向，打印结果 |
| [ai/transformer.py](../ai/transformer.py) / `Transformer.forward()` | 嵌入、位置编码、遮罩、Encoder/Decoder 堆叠、输出投影 |
| 同文件的 `EncoderLayer.forward()`、`DecoderLayer.forward()` | 按架构顺序连接注意力、FFN、残差和 LayerNorm |
| [ai/multihead_attention.py](../ai/multihead_attention.py) / `MultiHeadAttention.forward()` | 投影、拆头、合头，显式接收 Q/K/V，支持 self/cross-attention |
| [ai/attention.py](../ai/attention.py) / `attention()` | 手写缩放点积、数值稳定的 masked softmax、加权求和 |
| [ai/feed_forward.py](../ai/feed_forward.py) / `FeedForward.forward()` | 对每个位置独立执行 `D -> d_ff -> D` |
| [ai/layer_norm.py](../ai/layer_norm.py) / `layer_norm()` | 按特征维求均值、方差及归一化 |

```bash
python transformer_demo.py
python transformer_demo.py --d-model 16 --heads 4 --d-ff 64 --layers 2 --seed 7
python transformer_demo.py --source '[[2,5,7,0]]' --target '[[1,8,9]]'
```

模型默认 `d_model=32`、`heads=4`、`d_ff=4*d_model`、编码器和解码器各 2 层、`pad_id=0`。
演示默认两个词表各 32 项，可通过 `--src-vocab-size`、`--tgt-vocab-size` 修改。
`--layers` 控制两端各自的层数；各层参数独立。`--seed` 固定初始化便于调试。
`d_model` 必须被 `heads` 整除。

## 从一段输入走到输出

约定 `B` 是批大小、`S` 是源长度、`T` 是目标长度、`D` 是特征维度，`V` 是目标词表大小。

```text
source [B,S]                           target [B,T]（已右移）
     ↓                                     ↓
Embedding × sqrt(D) + Position         Embedding × sqrt(D) + Position
     ↓ [B,S,D]                             ↓ [B,T,D]
┌─ EncoderLayer，重复 N 次 ─┐          ┌─ DecoderLayer，重复 N 次 ─┐
│ 双向多头自注意力           │          │ 因果多头自注意力           │
│ 残差相加 → LayerNorm       │          │ 残差相加 → LayerNorm       │
│ FFN                      │          │ 交叉注意力 ← memory(K,V)  │
│ 残差相加 → LayerNorm       │          │ 残差相加 → LayerNorm       │
└──────────────────────────┘          │ FFN                      │
     ↓ memory [B,S,D]                  │ 残差相加 → LayerNorm       │
     └──────────────────────────────→ └──────────────────────────┘
                                           ↓ [B,T,D]
                                      Linear → logits [B,T,V]
                                           ↓（仅展示时）
                                      Softmax → probabilities
```

每个残差步骤保持 `D` 不变，因此可以直接相加。Post-LN 的顺序为
`LayerNorm(x + Sublayer(x))`，源码每一个加号都对应图中的一次残差相加。

## 多头注意力在做什么

`MultiHeadAttention.forward(query, key, value, mask)` 的输入尚未投影。
自注意力把同一个 `x` 传三次；交叉注意力传解码器 `x` 和两次编码器 `memory`。
这里令 `H` 为头数、`dh=D/H`：

| 步骤 | 形状变化 |
|---|---|
| `query @ wq` | `[B,Tq,D] -> [B,Tq,D]` |
| reshape 再 transpose | `[B,Tq,D] -> [B,H,Tq,dh]` |
| `key @ wk`、`value @ wv` 后拆头 | `[B,Tk,D] -> [B,H,Tk,dh]` |
| `Q @ K.transpose(...) / sqrt(dh)` | `[B,H,Tq,Tk]`，每行是一个 query 对各 key 的分数 |
| 遮罩并沿最后一维 softmax | `[B,H,Tq,Tk]`，仅允许的位置参与分配权重 |
| 权重乘 V | `[B,H,Tq,dh]` |
| transpose 再 reshape 合头 | `[B,Tq,D]` |
| 乘 `wo` | `[B,Tq,D]` |

除以的是 `sqrt(dh)`，因为每个头独立计算长度为 `dh` 的点积。
合头前需要 transpose；直接 reshape 会混淆 head 与 sequence 的顺序。
现有 `multihead_attention()` 函数保留 MHA/MQA/GQA 的统一练习，新类专注于标准 MHA 的组装。

## FFN 为什么不混合单词

```python
hidden = np.maximum(x @ self.w1 + self.b1, 0)
output = hidden @ self.w2 + self.b2
```

输入 `[B,T,D]` 变成 `[B,T,d_ff]`，再变回 `[B,T,D]`。
矩阵乘法只作用在最后的特征维；各 token 使用相同的权重，互相之间不读取数据。
Attention 负责位置间的信息交换，FFN 对每个位置的特征做非线性变换。

## 遮罩与右移目标

本项目约定布尔 `mask=True` 表示允许读取，`False` 表示禁止。
自定义 MHA mask 可传 `[Tq,Tk]`，或可广播到 `[B,H,Tq,Tk]` 的四维数组。
不要直接把 `[B,Tk]` 传入；padding mask 应扩成 `[B,1,1,Tk]`。

源 padding 遮罩同时用于 Encoder 自注意力和 Decoder 交叉注意力。
Decoder 自注意力使用目标 padding 与下三角因果遮罩的交集：

```text
目标长度 3 时（行是 query，列是 key）：
True  False False
True  True  False
True  True  True
```

下三角允许读取当前输入位置，所以预测下一个 token 时需要调用方先右移：

```text
正确目标：      [8,   9,   EOS]
Decoder 输入： [BOS, 8,   9  ]
模型各位置预测：[8,   9,   EOS]
```

`forward` 不会帮你右移。若直接把正确目标传入，就可能从当前输入读到答案。
示例用 1 表示 BOS，但 BOS 不写死在模型中。padding 只屏蔽 key；padding query
仍可能产生非零 logits，计算损失或展示预测时应忽略这些位置。
整行 key 全被屏蔽时，注意力输出为零；残差与 FFN 之后的模型输出不一定为零。

## 断点与验证

建议先运行小配置 `--d-model 8 --heads 2 --d-ff 16 --layers 1`。
在 `Transformer.forward()` 的 `memory = ...`、`decoded = ...` 以及各层的 `attended = ...`
处打断点，用 F11 跟进 MHA，观察 `q.shape`、`k.shape`、`v.shape`、`mask`。
进入 `attention()` 后观察 `scores`、`weights`，再回到 MHA 看 `merged.shape`。
进入 FFN 后观察 `hidden.shape`。按 F10 可查看残差相加和归一化前后的数值变化。

```bash
python -X utf8 -m unittest tests.test_ai tests.test_transformer -v
python -X utf8 -m unittest discover -s tests -v
```

测试使用手算值校验 MHA、FFN 和层连接，另验证未来 token 隔离、padding 隔离、
跨样本隔离、全遮罩数值稳定、初始化可复现、输入边界和命令行入口。
没有使用框架的 Attention/Transformer 层充当实现。

单层计算量为 `O(B[(S+T)(D²+D*d_ff)+(S²+T²+ST)D])`，最后的词表投影为
`O(BTDV)`。注意力矩阵占 `O(BH*max(S²,T²,ST))` 临时空间；此外还需嵌入、FFN 激活、
参数和 `[B,T,V]` 输出的空间。这里显式保存注意力矩阵，便于学习，不是 FlashAttention。
