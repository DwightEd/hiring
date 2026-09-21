"""旋转位置编码 RoPE
分类：Transformer
题意：x 为 ...×T×D，D 为偶数，positions 为 T 个绝对位置。
思路：相邻偶奇维按位置相关角度旋转；保持范数，点积只依赖相对角度。
复杂度：O(TD) 每个前导样本；同量级输出空间。
来源性质：通用算法手撕练习；具体公司出处仅以 companies/README.md 的映射为准。
"""

import numpy as np

def rope(x, positions=None, base=10000.0):
    x = np.asarray(x, dtype=float)
    t, d = x.shape[-2:]
    if d % 2:
        raise ValueError('旋转维度必须为偶数')
    positions = np.arange(t) if positions is None else np.asarray(positions)
    angles = positions[:, None] * base ** (-np.arange(0, d, 2) / d)
    cosine, sine = np.cos(angles), np.sin(angles)
    result = np.empty_like(x)
    result[..., 0::2] = x[..., 0::2] * cosine - x[..., 1::2] * sine
    result[..., 1::2] = x[..., 0::2] * sine + x[..., 1::2] * cosine
    return result
