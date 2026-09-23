"""Transformer 的逐位置前馈网络（FFN）。

输入 x: ...×D，输出同形状；所有 token 使用同一组权重，但不混合 token。
FFN(x) = ReLU(xW1 + b1)W2 + b2，隐层宽度 d_ff 通常为 4D。
时间 O(BTD·d_ff)，中间激活空间 O(BT·d_ff)，参数 O(D·d_ff)。
仅实现前向，便于手推维度；原理见 Attention Is All You Need 第 3.3 节。
"""

import numpy as np


class FeedForward:
    def __init__(self, d_model: int, d_ff: int, rng: np.random.Generator | None = None):
        if d_model <= 0 or d_ff <= 0:
            raise ValueError('d_model 和 d_ff 必须为正整数')
        rng = np.random.default_rng() if rng is None else rng
        self.w1 = rng.normal(0, 1 / np.sqrt(d_model), (d_model, d_ff))
        self.b1 = np.zeros(d_ff)
        self.w2 = rng.normal(0, 1 / np.sqrt(d_ff), (d_ff, d_model))
        self.b2 = np.zeros(d_model)

    def forward(self, x: np.ndarray) -> np.ndarray:
        """只沿最后的特征维做变换，保留 batch 和 sequence 维度。"""
        hidden = np.maximum(x @ self.w1 + self.b1, 0)
        return hidden @ self.w2 + self.b2
