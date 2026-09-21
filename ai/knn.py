"""K 近邻分类
分类：机器学习
题意：x 为 N×D 训练样本，labels 为整数标签，queries 为 M×D。
思路：平方距离选 k 个邻居，票数相同取较小标签；距离并列按训练下标。
复杂度：O(M(ND+N log N)) 时间，O(ND) 临时空间；可用选择算法优化排序。
来源性质：通用算法手撕练习；具体公司出处仅以 companies/README.md 的映射为准。
"""

import numpy as np

def knn(x, labels, queries, k=3):
    x, labels = np.asarray(x, dtype=float), np.asarray(labels)
    if not 1 <= k <= len(x):
        raise ValueError('k 越界')
    result = []
    for query in np.asarray(queries):
        distances = np.sum((x - query) ** 2, axis=1)
        nearest = np.argsort(distances, kind='stable')[:k]
        values, counts = np.unique(labels[nearest], return_counts=True)
        result.append(values[np.argmax(counts)])
    return np.asarray(result)
