"""两层 ReLU 网络手写反向传播
分类：神经网络
题意：x 为 N×D，W1 为 D×H，W2 为 H×C，类别标签为 N；返回 CE 和全部参数梯度。
思路：链式法则逐层传递，ReLU 在零处导数约定为零；不用自动微分。
复杂度：O(NDH+NHC) 时间，O(NH+NC) 激活空间。
来源性质：通用算法手撕练习；具体公司出处仅以 companies/README.md 的映射为准。
"""

import numpy as np
from ai.cross_entropy import cross_entropy

def loss_and_gradients(x, labels, w1, b1, w2, b2):
    hidden_pre = x @ w1 + b1
    hidden = np.maximum(hidden_pre, 0)
    loss, dlogits = cross_entropy(hidden @ w2 + b2, labels)
    dw2, db2 = hidden.T @ dlogits, dlogits.sum(axis=0)
    dh = (dlogits @ w2.T) * (hidden_pre > 0)
    return loss, (x.T @ dh, dh.sum(axis=0), dw2, db2)
