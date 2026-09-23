"""MHA、MQA、GQA 统一实现
分类：Transformer
题意：x 为 B×T×D，Q 头数 H，KV 头数 G 且 H%G=0；传入各投影矩阵，可选因果遮罩。
思路：投影后显式拆头，G 个 KV 头供各组 Q 头共享，再合并投影。
复杂度：O(BTD²+BT²D) 常规稠密计算；O(BHT²) 注意力空间。
来源性质：通用算法手撕练习；具体公司出处仅以 companies/README.md 的映射为准。

MultiHeadAttention 类是标准多头版，独立传入 Q/K/V，支持不同长度的交叉注意力。
阅读顺序：forward 中的投影 -> 拆头 -> 缩放点积注意力 -> 合头 -> 输出投影。
"""

import numpy as np
from ai.attention import attention

def multihead_attention(x, wq, wk, wv, wo, heads, kv_heads=None, causal=True):
    b, t, d = x.shape
    kv_heads = heads if kv_heads is None else kv_heads
    if d % heads or heads % kv_heads:
        raise ValueError('D 必须是 H 的整数倍，H 必须是 KV 头数的整数倍')
    width = d // heads
    q = (x @ wq).reshape(b, t, heads, width).transpose(0, 2, 1, 3)
    k = (x @ wk).reshape(b, t, kv_heads, width).transpose(0, 2, 1, 3)
    v = (x @ wv).reshape(b, t, kv_heads, width).transpose(0, 2, 1, 3)
    # 手撕版复制 KV 便于理解；生产内核可用分组广播避免实际复制。
    k, v = np.repeat(k, heads // kv_heads, axis=1), np.repeat(v, heads // kv_heads, axis=1)
    mask = np.tril(np.ones((t, t), dtype=bool)) if causal else None
    output, _ = attention(q, k, v, mask)
    return output.transpose(0, 2, 1, 3).reshape(b, t, d) @ wo


class MultiHeadAttention:
    """无偏置的标准 MHA；参数矩阵均为 D×D，可直接查看或赋值。"""

    def __init__(self, d_model: int, heads: int, rng: np.random.Generator | None = None):
        if d_model <= 0 or heads <= 0 or d_model % heads:
            raise ValueError('d_model 和 heads 必须为正整数，且 d_model 能被 heads 整除')
        self.d_model = d_model
        self.heads = heads
        self.head_dim = d_model // heads
        rng = np.random.default_rng() if rng is None else rng
        scale = 1 / np.sqrt(d_model)
        self.wq = rng.normal(0, scale, (d_model, d_model))
        self.wk = rng.normal(0, scale, (d_model, d_model))
        self.wv = rng.normal(0, scale, (d_model, d_model))
        self.wo = rng.normal(0, scale, (d_model, d_model))

    def _split_heads(self, x: np.ndarray) -> np.ndarray:
        batch, length, _ = x.shape
        # B×T×D -> B×T×H×dh -> B×H×T×dh。
        return x.reshape(batch, length, self.heads, self.head_dim).transpose(0, 2, 1, 3)

    def forward(
        self, query: np.ndarray, key: np.ndarray, value: np.ndarray,
        mask: np.ndarray | None = None,
    ) -> np.ndarray:
        """Q: B×Tq×D，K/V: B×Tk×D，返回 B×Tq×D。

        mask 为布尔数组，True 表示允许；支持 Tq×Tk 或可广播到 B×H×Tq×Tk
        的四维形状（如 B×1×1×Tk 的 padding mask）。全遮罩行输出零。
        自注意力传入同一个 x 三次；交叉注意力的 Q 来自解码器，K/V 来自编码器。
        """
        for x in (query, key, value):
            if x.ndim != 3 or x.shape[-1] != self.d_model or x.shape[1] == 0:
                raise ValueError('Q/K/V 必须为 B×T×d_model，且序列非空')
        if key.shape != value.shape or query.shape[0] != key.shape[0]:
            raise ValueError('Q/K/V 的 batch 必须相同，K/V 的形状必须相同')
        if mask is not None:
            mask = np.asarray(mask)
            if mask.dtype != np.bool_ or mask.ndim not in (2, 4):
                raise ValueError('mask 必须为二维或四维布尔数组，True 表示允许')

        q = self._split_heads(query @ self.wq)
        k = self._split_heads(key @ self.wk)
        v = self._split_heads(value @ self.wv)
        # attention 内部手写 QKᵀ/sqrt(dh)、masked softmax 和权重乘 V。
        attended, _ = attention(q, k, v, mask)
        batch, _, query_length, _ = attended.shape
        merged = attended.transpose(0, 2, 1, 3).reshape(batch, query_length, self.d_model)
        return merged @ self.wo
