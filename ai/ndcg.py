"""NDCG@K
分类：评估指标
题意：输入每个候选的非负相关性与预测分数；分数平局按原下标稳定排序。
思路：使用增益 2^rel-1 和 log2(rank+1) 折扣，除以理想排序 DCG。
复杂度：O(n log n) 时间，O(n) 空间。
来源性质：通用算法手撕练习；具体公司出处仅以 companies/README.md 的映射为准。
"""

from math import log2

def ndcg(relevance, scores, k):
    if k <= 0:
        return 0.0
    order = sorted(range(len(scores)), key=lambda i: (-scores[i], i))[:k]
    ideal = sorted(relevance, reverse=True)[:k]
    dcg = sum((2**relevance[index] - 1) / log2(rank + 2) for rank, index in enumerate(order))
    idcg = sum((2**value - 1) / log2(rank + 2) for rank, value in enumerate(ideal))
    return dcg / idcg if idcg else 0.0
