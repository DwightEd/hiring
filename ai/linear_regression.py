"""线性回归梯度下降
分类：机器学习
题意：x 为 N×D，y 为 N，返回权重、偏置与损失历史。
思路：MSE 的梯度为 2Xᵀ(Xw+b-y)/N；学习率需与数据尺度匹配。
复杂度：O(iter·ND) 时间，O(N+D) 辅助空间及迭代记录。
来源性质：通用算法手撕练习；具体公司出处仅以 companies/README.md 的映射为准。
"""

import numpy as np

def fit(x, y, learning_rate=0.01, steps=1000):
    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
    weight, bias, history = np.zeros(x.shape[1]), 0.0, []
    for _ in range(steps):
        residual = x @ weight + bias - y
        history.append(float(np.mean(residual**2)))
        weight -= learning_rate * 2 * (x.T @ residual) / len(x)
        bias -= learning_rate * 2 * residual.mean()
    return weight, bias, history
