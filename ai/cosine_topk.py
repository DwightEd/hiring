"""余弦相似度 Top-k 检索
分类：检索排序
题意：输入一个 D 维 query 和 N×D 文档，返回得分降序的下标及分数。
思路：先归一化再点积；零向量约定相似度为零；平分按下标。
复杂度：O(ND+N log N) 时间，O(ND) 空间。
来源性质：通用算法手撕练习；具体公司出处仅以 companies/README.md 的映射为准。
"""

import numpy as np

def cosine_topk(query, documents, k):
    query, documents = np.asarray(query, dtype=float), np.asarray(documents, dtype=float)
    denominator = np.linalg.norm(documents, axis=1) * np.linalg.norm(query)
    scores = np.divide(documents @ query, denominator, out=np.zeros(len(documents)), where=denominator != 0)
    order = np.argsort(-scores, kind='stable')[:k]
    return order, scores[order]
