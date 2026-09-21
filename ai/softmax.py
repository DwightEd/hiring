"""稳定 Softmax 与反向传播
分类：数值计算
题意：输入任意维 logits，在指定轴归一化；返回概率。反向接收概率 p 与上游梯度 g。
思路：减去最大值防溢出；Jᵀg=p*(g-sum(g*p))，无需构造雅可比矩阵。
复杂度：O(N) 时间和空间。
来源性质：通用算法手撕练习；具体公司出处仅以 companies/README.md 的映射为准。
"""

import numpy as np

def softmax(x, axis=-1):
    x = np.asarray(x, dtype=float)
    shifted = x - np.max(x, axis=axis, keepdims=True)
    exp = np.exp(shifted)
    return exp / exp.sum(axis=axis, keepdims=True)

def backward(p, grad, axis=-1):
    return p * (grad - np.sum(grad * p, axis=axis, keepdims=True))
