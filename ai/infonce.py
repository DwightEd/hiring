"""对比学习 InfoNCE
分类：损失函数
题意：queries 与 keys 都是 N×D，同下标为正对，其余是批内负样本。
思路：L2 归一化后计算相似度矩阵，除温度，对角标签做 CE。
复杂度：O(N²D) 时间，O(N²+ND) 空间。
来源性质：通用算法手撕练习；具体公司出处仅以 companies/README.md 的映射为准。
"""

import numpy as np
from ai.cross_entropy import cross_entropy

def infonce(queries, keys, temperature=0.1):
    if temperature <= 0:
        raise ValueError('temperature 必须为正')
    q = queries / np.maximum(np.linalg.norm(queries, axis=1, keepdims=True), 1e-12)
    k = keys / np.maximum(np.linalg.norm(keys, axis=1, keepdims=True), 1e-12)
    return cross_entropy(q @ k.T / temperature, np.arange(len(q)))[0]
