"""缩放点积注意力和反向传播
分类：Transformer
题意：Q/K/V 形状为 ...×Tq×d、...×Tk×d、...×Tk×dv；mask=True 表示允许。全遮罩行输出零。Q/K/V 的前导批次形状须相同；仅 mask 支持广播。
思路：QKᵀ/sqrt(d)，屏蔽后按行 softmax，再乘 V；链式求导得到 dQ,dK,dV。
复杂度：O(Tq·Tk·(d+dv)) 时间，O(Tq·Tk) 注意力空间。
来源性质：通用算法手撕练习；具体公司出处仅以 companies/README.md 的映射为准。
"""

import numpy as np

def attention(q, k, v, mask=None):
    scores = q @ np.swapaxes(k, -1, -2) / np.sqrt(q.shape[-1])
    allowed = np.ones_like(scores, dtype=bool) if mask is None else np.broadcast_to(mask, scores.shape)
    scores = np.where(allowed, scores, -np.inf)
    maximum = scores.max(axis=-1, keepdims=True)
    maximum = np.where(np.isfinite(maximum), maximum, 0.0)
    exp = np.exp(scores - maximum)
    denominator = exp.sum(axis=-1, keepdims=True)
    weights = np.divide(exp, denominator, out=np.zeros_like(exp), where=denominator != 0)
    return weights @ v, (q, k, v, weights)

def backward(grad, cache):
    q, k, v, weights = cache
    dv = np.swapaxes(weights, -1, -2) @ grad
    da = grad @ np.swapaxes(v, -1, -2)
    ds = weights * (da - np.sum(da * weights, axis=-1, keepdims=True))
    ds /= np.sqrt(q.shape[-1])
    return ds @ k, np.swapaxes(ds, -1, -2) @ q, dv
