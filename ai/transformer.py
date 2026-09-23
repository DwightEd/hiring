"""手写 Encoder–Decoder Transformer：NumPy 前向 / 推理教学实现。

采用 Attention Is All You Need 第 3 节的 Post-LN、ReLU FFN、正弦位置编码。
Dropout 在推理时为恒等；此文件不实现训练、自动微分或 KV cache。
阅读顺序：Transformer.forward -> EncoderLayer/DecoderLayer.forward -> MHA/FFN。
参数均为普通 NumPy 数组，每层独立初始化，方便在调试器里观察。
架构来源：https://arxiv.org/abs/1706.03762
"""

import numpy as np

from ai.feed_forward import FeedForward
from ai.layer_norm import layer_norm
from ai.multihead_attention import MultiHeadAttention


def positional_encoding(length: int, d_model: int) -> np.ndarray:
    """返回 T×D；偶数维 sin，奇数维 cos，不包含可训练参数。"""
    if length <= 0 or d_model <= 0:
        raise ValueError('length 和 d_model 必须为正整数')
    positions = np.arange(length)[:, None]
    frequencies = 10000.0 ** (-np.arange(0, d_model, 2) / d_model)
    angles = positions * frequencies
    encoding = np.zeros((length, d_model))
    encoding[:, 0::2] = np.sin(angles)
    encoding[:, 1::2] = np.cos(angles[:, :d_model // 2])
    return encoding


class LayerNorm:
    """每个子层独立保存 gamma/beta；沿最后一维归一化。"""

    def __init__(self, d_model: int):
        self.gamma = np.ones(d_model)
        self.beta = np.zeros(d_model)

    def forward(self, x: np.ndarray) -> np.ndarray:
        output, _ = layer_norm(x, self.gamma, self.beta)
        return output


class EncoderLayer:
    def __init__(self, d_model: int, heads: int, d_ff: int, rng: np.random.Generator):
        self.self_attention = MultiHeadAttention(d_model, heads, rng)
        self.ffn = FeedForward(d_model, d_ff, rng)
        self.norm1 = LayerNorm(d_model)
        self.norm2 = LayerNorm(d_model)

    def forward(self, x: np.ndarray, mask: np.ndarray | None = None) -> np.ndarray:
        """双向自注意力 -> Add & Norm -> FFN -> Add & Norm。"""
        attended = self.self_attention.forward(x, x, x, mask)
        x = self.norm1.forward(x + attended)
        return self.norm2.forward(x + self.ffn.forward(x))


class DecoderLayer:
    def __init__(self, d_model: int, heads: int, d_ff: int, rng: np.random.Generator):
        self.self_attention = MultiHeadAttention(d_model, heads, rng)
        self.cross_attention = MultiHeadAttention(d_model, heads, rng)
        self.ffn = FeedForward(d_model, d_ff, rng)
        self.norm1 = LayerNorm(d_model)
        self.norm2 = LayerNorm(d_model)
        self.norm3 = LayerNorm(d_model)

    def forward(
        self, x: np.ndarray, memory: np.ndarray,
        self_mask: np.ndarray | None = None, memory_mask: np.ndarray | None = None,
    ) -> np.ndarray:
        """遮罩自注意力 -> 交叉注意力 -> FFN；每步都有残差和 Post-LN。

        self_mask 由调用方传入因果遮罩；交叉注意力 Q 来自解码器，K/V 来自 memory。
        """
        attended = self.self_attention.forward(x, x, x, self_mask)
        x = self.norm1.forward(x + attended)
        attended = self.cross_attention.forward(x, memory, memory, memory_mask)
        x = self.norm2.forward(x + attended)
        return self.norm3.forward(x + self.ffn.forward(x))


class Transformer:
    """完整前向：token IDs -> 嵌入和位置 -> 编码/解码堆叠 -> 词表 logits。

    仅推理模式，无训练循环；源/目标嵌入与输出投影各自独立，不共享权重。
    构造器的 seed 控制全部参数初始化，d_ff 缺省为 4*d_model。
    """

    def __init__(
        self, src_vocab_size: int, tgt_vocab_size: int, d_model: int = 32,
        heads: int = 4, d_ff: int | None = None, num_layers: int = 2,
        pad_id: int = 0, seed: int = 0,
    ):
        d_ff = 4 * d_model if d_ff is None else d_ff
        if min(src_vocab_size, tgt_vocab_size, d_model, heads, d_ff, num_layers) <= 0:
            raise ValueError('词表、维度、头数和层数必须为正整数')
        if d_model % heads:
            raise ValueError('d_model 必须能被 heads 整除')
        if not 0 <= pad_id < min(src_vocab_size, tgt_vocab_size):
            raise ValueError('pad_id 必须位于源和目标词表内')
        self.d_model = d_model
        self.pad_id = pad_id
        rng = np.random.default_rng(seed)
        scale = 1 / np.sqrt(d_model)
        self.src_embedding = rng.normal(0, scale, (src_vocab_size, d_model))
        self.tgt_embedding = rng.normal(0, scale, (tgt_vocab_size, d_model))
        self.encoder_layers = [EncoderLayer(d_model, heads, d_ff, rng) for _ in range(num_layers)]
        self.decoder_layers = [DecoderLayer(d_model, heads, d_ff, rng) for _ in range(num_layers)]
        self.output_weight = rng.normal(0, scale, (d_model, tgt_vocab_size))
        self.output_bias = np.zeros(tgt_vocab_size)

    def forward(self, source: np.ndarray, target: np.ndarray) -> np.ndarray:
        """source: B×S，target: B×T，返回 B×T×V 的未归一化 logits。

        target 是调用方右移后的解码器输入，例如 [BOS,y0,y1]，预测 [y0,y1,EOS]。
        pad_id 仅屏蔽 key；padding query 的 logits 不参与训练损失或有效输出。
        序列可以不同长度，batch 必须一致。输入不会被修改。
        """
        source, target = np.asarray(source), np.asarray(target)
        for name, tokens, embedding in (
            ('source', source, self.src_embedding), ('target', target, self.tgt_embedding),
        ):
            if tokens.ndim != 2 or 0 in tokens.shape:
                raise ValueError(f'{name} 必须为非空 B×T 数组')
            if not np.issubdtype(tokens.dtype, np.integer):
                raise ValueError(f'{name} 必须包含整数 token ID')
            if np.any(tokens < 0) or np.any(tokens >= len(embedding)):
                raise ValueError(f'{name} 的 token ID 超出词表')
        if source.shape[0] != target.shape[0]:
            raise ValueError('source 和 target 的 batch 必须相同')

        # True 表示可读。源 padding 遮罩用于 encoder self-attention 和 decoder cross-attention。
        source_mask = (source != self.pad_id)[:, None, None, :]
        target_length = target.shape[1]
        causal_mask = np.tril(np.ones((target_length, target_length), dtype=bool))
        target_mask = causal_mask[None, None, :, :] & (target != self.pad_id)[:, None, None, :]

        memory = self.src_embedding[source] * np.sqrt(self.d_model)
        memory = memory + positional_encoding(source.shape[1], self.d_model)
        for layer in self.encoder_layers:
            memory = layer.forward(memory, source_mask)

        decoded = self.tgt_embedding[target] * np.sqrt(self.d_model)
        decoded = decoded + positional_encoding(target_length, self.d_model)
        for layer in self.decoder_layers:
            decoded = layer.forward(decoded, memory, target_mask, source_mask)

        return decoded @ self.output_weight + self.output_bias
