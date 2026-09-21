"""Adam 参数更新
分类：优化器
题意：保存同形状的一阶、二阶动量，步数从 1 开始，返回新参数。
思路：指数动量加偏差校正；epsilon 放在 sqrt(v_hat) 外。
复杂度：每步 O(P) 时间和空间。
来源性质：通用算法手撕练习；具体公司出处仅以 companies/README.md 的映射为准。
"""

import numpy as np

class Adam:
    def __init__(self, shape, learning_rate=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
        self.m, self.v = np.zeros(shape), np.zeros(shape)
        self.t, self.lr, self.b1, self.b2, self.eps = 0, learning_rate, beta1, beta2, eps

    def step(self, parameter, gradient):
        self.t += 1
        self.m = self.b1*self.m + (1-self.b1)*gradient
        self.v = self.b2*self.v + (1-self.b2)*gradient**2
        mhat, vhat = self.m/(1-self.b1**self.t), self.v/(1-self.b2**self.t)
        return parameter - self.lr*mhat/(np.sqrt(vhat)+self.eps)
