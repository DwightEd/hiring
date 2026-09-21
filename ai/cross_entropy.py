"""多分类交叉熵及梯度
分类：损失函数
题意：logits 为 N×C，labels 为 N 个类别编号；返回平均损失及 logits 梯度。
思路：使用 log-sum-exp，梯度为 (softmax-one_hot)/N。
复杂度：O(NC) 时间和空间。
来源性质：通用算法手撕练习；具体公司出处仅以 companies/README.md 的映射为准。
"""

import numpy as np

def cross_entropy(logits, labels):
    logits = np.asarray(logits, dtype=float)
    labels = np.asarray(labels, dtype=int)
    shifted = logits - logits.max(axis=1, keepdims=True)
    exp = np.exp(shifted)
    normalizer = exp.sum(axis=1, keepdims=True)
    loss = np.mean(np.log(normalizer[:, 0]) - shifted[np.arange(len(labels)), labels])
    grad = exp / normalizer
    grad[np.arange(len(labels)), labels] -= 1
    return float(loss), grad / len(labels)
