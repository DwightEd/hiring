"""RMSNorm
分类：归一化
题意：x 最后一维为特征，weight 为缩放；不减均值。
思路：按均方根缩放，与 LayerNorm 的去均值步骤不同。
复杂度：O(ND) 时间和空间。
来源性质：通用算法手撕练习；具体公司出处仅以 companies/README.md 的映射为准。
"""

import numpy as np

def rms_norm(x, weight, eps=1e-6):
    x = np.asarray(x, dtype=float)
    return x * weight / np.sqrt(np.mean(x * x, axis=-1, keepdims=True) + eps)
