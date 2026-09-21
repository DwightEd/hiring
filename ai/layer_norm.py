"""LayerNorm 前向与反向
分类：归一化
题意：x 最后一维为特征，gamma/beta 长度 D；返回 y 与缓存。
思路：对每个样本的特征维求均值和总体方差；反向保留投影到常数和归一化向量的修正项。
复杂度：O(ND) 时间和空间。
来源性质：通用算法手撕练习；具体公司出处仅以 companies/README.md 的映射为准。
"""

import numpy as np

def layer_norm(x, gamma, beta, eps=1e-5):
    centered = x - x.mean(axis=-1, keepdims=True)
    inverse = 1 / np.sqrt(np.mean(centered ** 2, axis=-1, keepdims=True) + eps)
    normalized = centered * inverse
    return normalized * gamma + beta, (normalized, inverse, gamma)

def backward(grad, cache):
    normalized, inverse, gamma = cache
    g = grad * gamma
    dx = inverse * (g - g.mean(axis=-1, keepdims=True) - normalized * (g * normalized).mean(axis=-1, keepdims=True))
    axes = tuple(range(grad.ndim - 1))
    return dx, np.sum(grad * normalized, axis=axes), np.sum(grad, axis=axes)
