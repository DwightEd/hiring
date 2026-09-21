"""Top-k、Top-p 与温度采样
分类：解码
题意：输入一维有限 logits，temperature>0，top_k 可选，0<top_p<=1；返回 token 与过滤后概率。
思路：先温度缩放、Top-k，再按概率累积保留跨过 p 的那一项，重新归一化。
复杂度：O(V log V) 时间，O(V) 空间；完整排序便于确定平分规则。
来源性质：通用算法手撕练习；具体公司出处仅以 companies/README.md 的映射为准。
"""

import numpy as np

def sample(logits, temperature=1.0, top_k=None, top_p=1.0, seed=None):
    if temperature <= 0 or not 0 < top_p <= 1:
        raise ValueError('temperature>0 且 0<top_p<=1')
    logits = np.asarray(logits, dtype=float) / temperature
    order = np.argsort(-logits, kind='stable')
    if top_k is not None:
        if not 1 <= top_k <= len(logits):
            raise ValueError('top_k 越界')
        order = order[:top_k]
    probabilities = np.exp(logits[order] - logits[order[0]])
    probabilities /= probabilities.sum()
    if top_p < 1:
        count = min(len(order), np.searchsorted(np.cumsum(probabilities), top_p) + 1)
        order, probabilities = order[:count], probabilities[:count]
        probabilities /= probabilities.sum()
    full = np.zeros(len(logits))
    full[order] = probabilities
    return int(np.random.default_rng(seed).choice(len(logits), p=full)), full
