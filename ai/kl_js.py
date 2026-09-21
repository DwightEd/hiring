"""KL 与 JS 散度
分类：信息论
题意：p、q 为非负且和为 1 的一维概率向量；使用自然对数。
思路：p=0 项贡献零；p>0 且 q=0 时 KL 为无穷；JS 用混合分布。
复杂度：O(n) 时间，O(n) 临时空间。
来源性质：通用算法手撕练习；具体公司出处仅以 companies/README.md 的映射为准。
"""

import numpy as np

def kl(p, q):
    p, q = np.asarray(p, dtype=float), np.asarray(q, dtype=float)
    positive = p > 0
    if np.any(q[positive] == 0):
        return float('inf')
    return float(np.sum(p[positive] * np.log(p[positive] / q[positive])))

def js(p, q):
    p, q = np.asarray(p, dtype=float), np.asarray(q, dtype=float)
    middle = (p + q) / 2
    return (kl(p, middle) + kl(q, middle)) / 2
