"""Inverted Dropout
分类：神经网络
题意：p 为丢弃概率，0<=p<1，训练随机丢弃并缩放，推理恒等。
思路：除以保留概率让输出期望不变，反向复用同一个掩码。
复杂度：O(N) 时间和空间。
来源性质：通用算法手撕练习；具体公司出处仅以 companies/README.md 的映射为准。
"""

import numpy as np

def dropout(x, p=0.5, training=True, seed=None):
    if not 0 <= p < 1:
        raise ValueError('要求 0<=p<1')
    if not training:
        return x.copy(), np.ones_like(x)
    mask = (np.random.default_rng(seed).random(x.shape) >= p) / (1-p)
    return x * mask, mask

def backward(grad, mask):
    return grad * mask
