"""稳定 Sigmoid 与二分类交叉熵
分类：损失函数
题意：输入 logits 和同形状 0/1 标签；返回平均 BCE 与梯度。
思路：用 exp(-abs(x)) 避免 sigmoid 溢出，BCE 用 max(x,0)-xy+log1p(exp(-abs(x)))。
复杂度：O(N) 时间和空间。
来源性质：通用算法手撕练习；具体公司出处仅以 companies/README.md 的映射为准。
"""

import numpy as np

def sigmoid(x):
    x = np.asarray(x, dtype=float)
    z = np.exp(-np.abs(x))
    return np.where(x >= 0, 1 / (1 + z), z / (1 + z))

def binary_cross_entropy(logits, labels):
    x, y = np.asarray(logits, dtype=float), np.asarray(labels, dtype=float)
    loss = np.maximum(x, 0) - x * y + np.log1p(np.exp(-np.abs(x)))
    return float(loss.mean()), (sigmoid(x) - y) / x.size
