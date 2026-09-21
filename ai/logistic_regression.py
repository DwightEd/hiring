"""逻辑回归梯度下降
分类：机器学习
题意：输入 N×D 特征与二分类标签，返回权重和偏置；可选 L2 正则。
思路：从稳定 BCE 得到梯度，正则只作用于权重。
复杂度：O(iter·ND) 时间，O(N+D) 辅助空间。
来源性质：通用算法手撕练习；具体公司出处仅以 companies/README.md 的映射为准。
"""

import numpy as np
from ai.sigmoid_bce import sigmoid

def fit(x, y, learning_rate=0.1, steps=1000, l2=0.0):
    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
    weight, bias = np.zeros(x.shape[1]), 0.0
    for _ in range(steps):
        error = sigmoid(x @ weight + bias) - y
        weight -= learning_rate * (x.T @ error / len(x) + l2 * weight)
        bias -= learning_rate * error.mean()
    return weight, bias
