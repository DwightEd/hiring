# AI 算法手撕 · 36 模块

NumPy / 标准库实现：数值稳定性、维度、梯度、并列规则写在文件头。每个模块计一次，前向和反向不重复计数。运行测试需安装 requirements.txt。

[返回总目录](../README.md)

## 数值计算（1）

| 题目 / 代码 | 核心思路 | 复杂度 |
|---|---|---|
| [稳定 Softmax 与反向传播](../ai/softmax.py) | 减去最大值防溢出；Jᵀg=p*(g-sum(g*p))，无需构造雅可比矩阵。 | O(N) 时间和空间 |

## 损失函数（3）

| 题目 / 代码 | 核心思路 | 复杂度 |
|---|---|---|
| [多分类交叉熵及梯度](../ai/cross_entropy.py) | 使用 log-sum-exp，梯度为 (softmax-one_hot)/N。 | O(NC) 时间和空间 |
| [稳定 Sigmoid 与二分类交叉熵](../ai/sigmoid_bce.py) | 用 exp(-abs(x)) 避免 sigmoid 溢出，BCE 用 max(x,0)-xy+log1p(exp(-abs(x)))。 | O(N) 时间和空间 |
| [对比学习 InfoNCE](../ai/infonce.py) | L2 归一化后计算相似度矩阵，除温度，对角标签做 CE。 | O(N²D) 时间，O(N²+ND) 空间 |

## 归一化（3）

| 题目 / 代码 | 核心思路 | 复杂度 |
|---|---|---|
| [LayerNorm 前向与反向](../ai/layer_norm.py) | 对每个样本的特征维求均值和总体方差；反向保留投影到常数和归一化向量的修正项。 | O(ND) 时间和空间 |
| [RMSNorm](../ai/rms_norm.py) | 按均方根缩放，与 LayerNorm 的去均值步骤不同。 | O(ND) 时间和空间 |
| [BatchNorm 训练与推理](../ai/batch_norm.py) | 区分训练统计量与推理 running statistics，训练 batch 至少两个样本。 | 每次 O(ND) 时间、O(ND) 输出及临时空间 |

## Transformer（4）

| 题目 / 代码 | 核心思路 | 复杂度 |
|---|---|---|
| [缩放点积注意力和反向传播](../ai/attention.py) | QKᵀ/sqrt(d)，屏蔽后按行 softmax，再乘 V；链式求导得到 dQ,dK,dV。 | O(Tq·Tk·(d+dv)) 时间，O(Tq·Tk) 注意力空间 |
| [MHA、MQA、GQA 统一实现](../ai/multihead_attention.py) | 投影后显式拆头，G 个 KV 头供各组 Q 头共享，再合并投影。 | O(BTD²+BT²D) 常规稠密计算；O(BHT²) 注意力空间 |
| [旋转位置编码 RoPE](../ai/rope.py) | 相邻偶奇维按位置相关角度旋转；保持范数，点积只依赖相对角度。 | O(TD) 每个前导样本；同量级输出空间 |
| [LoRA 线性层及合并权重](../ai/lora.py) | 输出 xW+(alpha/r)(xA)B；合并时 W'=W+(alpha/r)AB。 | 附加 O(Nr(Din+Dout)) 时间，O(r(Din+Dout)) 参数 |

## 解码（2）

| 题目 / 代码 | 核心思路 | 复杂度 |
|---|---|---|
| [Top-k、Top-p 与温度采样](../ai/sampling.py) | 先温度缩放、Top-k，再按概率累积保留跨过 p 的那一项，重新归一化。 | O(V log V) 时间，O(V) 空间；完整排序便于确定平分规则 |
| [Beam Search](../ai/beam_search.py) | 累加对数概率，结束序列也保留在候选池；这里不用长度惩罚。 | O(T·B·V·(T+log(BV))) 教学实现，含复制与排序 |

## 机器学习（6）

| 题目 / 代码 | 核心思路 | 复杂度 |
|---|---|---|
| [K-means 聚类](../ai/kmeans.py) | Lloyd 交替最近中心分配与均值更新；空簇保持旧中心，返回前重新分配。 | O(iter·N·k·D) 时间，O(Nk+kD) 空间 |
| [K 近邻分类](../ai/knn.py) | 平方距离选 k 个邻居，票数相同取较小标签；距离并列按训练下标。 | O(M(ND+N log N)) 时间，O(ND) 临时空间；可用选择算法优化排序 |
| [线性回归梯度下降](../ai/linear_regression.py) | MSE 的梯度为 2Xᵀ(Xw+b-y)/N；学习率需与数据尺度匹配。 | O(iter·ND) 时间，O(N+D) 辅助空间及迭代记录 |
| [逻辑回归梯度下降](../ai/logistic_regression.py) | 从稳定 BCE 得到梯度，正则只作用于权重。 | O(iter·ND) 时间，O(N+D) 辅助空间 |
| [PCA 降维](../ai/pca.py) | 中心化后做 SVD；主方向符号不唯一，不能按符号判断正确性。 | O(ND·min(N,D)) 稠密 SVD，O(ND) 空间 |
| [高斯朴素贝叶斯](../ai/gaussian_nb.py) | 在 log 域累加概率，方差加平滑，避免连乘下溢与零方差。 | 此按类切片实现训练 O(CN+ND)，预测 O(MCD) |

## 评估指标（3）

| 题目 / 代码 | 核心思路 | 复杂度 |
|---|---|---|
| [ROC AUC](../ai/auc.py) | 升序分数组：每个正例胜过所有较低分负例，并与同分负例各计半胜。 | O(n log n) 时间，O(n) 空间 |
| [Average Precision](../ai/average_precision.py) | AP=sum(召回增量×当前精确率)，不把梯形 PR 面积误当 AP。 | O(n log n) 时间，O(n) 空间 |
| [NDCG@K](../ai/ndcg.py) | 使用增益 2^rel-1 和 log2(rank+1) 折扣，除以理想排序 DCG。 | O(n log n) 时间，O(n) 空间 |

## 检索排序（1）

| 题目 / 代码 | 核心思路 | 复杂度 |
|---|---|---|
| [余弦相似度 Top-k 检索](../ai/cosine_topk.py) | 先归一化再点积；零向量约定相似度为零；平分按下标。 | O(ND+N log N) 时间，O(ND) 空间 |

## 计算机视觉（5）

| 题目 / 代码 | 核心思路 | 复杂度 |
|---|---|---|
| [IoU 与 NMS](../ai/iou_nms.py) | 贪心保留最高分框，删除与之过度重叠的框；坐标面积不加一。 | NMS 最坏 O(N²)，O(N) 辅助空间 |
| [二维卷积前向](../ai/conv2d.py) | 实现深度学习中的互相关，不翻转卷积核；循环空间位置，einsum 聚合通道和核。 | O(N·O·Ho·Wo·I·Kh·Kw)，临时空间为补零输入及输出 |
| [最大池化前向与反向](../ai/max_pool2d.py) | 重叠窗口反向必须累加，不能直接覆盖。 | O(NC·HoWo·k²) 时间，缓存 O(NC·HoWo) |
| [Focal Loss](../ai/focal_loss.py) | 见代码逐步注释 | O(N) |
| [Gaussian Soft-NMS](../ai/soft_nms.py) | 见代码逐步注释 | O(N²) |

## 神经网络（2）

| 题目 / 代码 | 核心思路 | 复杂度 |
|---|---|---|
| [两层 ReLU 网络手写反向传播](../ai/mlp_backprop.py) | 链式法则逐层传递，ReLU 在零处导数约定为零；不用自动微分。 | O(NDH+NHC) 时间，O(NH+NC) 激活空间 |
| [Inverted Dropout](../ai/dropout.py) | 除以保留概率让输出期望不变，反向复用同一个掩码。 | O(N) 时间和空间 |

## 优化器（1）

| 题目 / 代码 | 核心思路 | 复杂度 |
|---|---|---|
| [Adam 参数更新](../ai/adam.py) | 指数动量加偏差校正；epsilon 放在 sqrt(v_hat) 外。 | 每步 O(P) 时间和空间 |

## 信息论（1）

| 题目 / 代码 | 核心思路 | 复杂度 |
|---|---|---|
| [KL 与 JS 散度](../ai/kl_js.py) | p=0 项贡献零；p>0 且 q=0 时 KL 为无穷；JS 用混合分布。 | O(n) 时间，O(n) 临时空间 |

## 强化学习（1）

| 题目 / 代码 | 核心思路 | 复杂度 |
|---|---|---|
| [PPO、DPO 与 GRPO 组内优势](../ai/rl_losses.py) | PPO 取 clipped surrogate 的较小者；DPO 对相对偏好 margin 做 log-sigmoid；组内标准化奖励。 | O(N) 时间和空间；实现的是核心目标，非完整训练器 |

## NLP（1）

| 题目 / 代码 | 核心思路 | 复杂度 |
|---|---|---|
| [简化 BPE 训练和编码](../ai/bpe.py) | 每轮合并最频繁一对，同频按字典序；编码严格重放合并规则。 | O(merges·总语料 token 数) 的基础实现；非生产 tokenizer |

## 随机算法（2）

| 题目 / 代码 | 核心思路 | 复杂度 |
|---|---|---|
| [蓄水池抽样](../ai/reservoir_sampling.py) | 第 i 项以 k/i 概率进入，随机替换池内一个位置。 | O(n) 时间，O(k) 空间 |
| [原地等概率洗牌](../ai/fisher_yates.py) | 从后往前，位置 i 与 [0,i] 均匀随机位置交换。 | O(n) 时间，O(1) 辅助空间 |
