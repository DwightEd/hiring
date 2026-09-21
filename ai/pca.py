"""PCA 降维
分类：机器学习
题意：输入 N×D，返回 N×k 投影、k×D 主方向、均值和 k 个解释方差。
思路：中心化后做 SVD；主方向符号不唯一，不能按符号判断正确性。
复杂度：O(ND·min(N,D)) 稠密 SVD，O(ND) 空间。
来源性质：通用算法手撕练习；具体公司出处仅以 companies/README.md 的映射为准。
"""

import numpy as np

def pca(x, k):
    x = np.asarray(x, dtype=float)
    if len(x) < 2 or not 1 <= k <= min(x.shape):
        raise ValueError('至少两个样本且 k 不超过 min(N,D)')
    mean = x.mean(axis=0)
    _, singular, vt = np.linalg.svd(x - mean, full_matrices=False)
    components = vt[:k]
    return (x - mean) @ components.T, components, mean, singular[:k]**2 / (len(x) - 1)
