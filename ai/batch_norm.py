"""BatchNorm 训练与推理
分类：归一化
题意：处理 N×D 输入；训练更新滑动均值和无偏方差，归一化使用有偏批方差。
思路：区分训练统计量与推理 running statistics，训练 batch 至少两个样本。
复杂度：每次 O(ND) 时间、O(ND) 输出及临时空间。
来源性质：通用算法手撕练习；具体公司出处仅以 companies/README.md 的映射为准。
"""

import numpy as np

class BatchNorm:
    def __init__(self, features, momentum=0.1, eps=1e-5):
        self.gamma, self.beta = np.ones(features), np.zeros(features)
        self.mean, self.variance = np.zeros(features), np.ones(features)
        self.momentum, self.eps = momentum, eps

    def __call__(self, x, training=True):
        x = np.asarray(x, dtype=float)
        if training:
            if len(x) < 2:
                raise ValueError('训练批次至少需要两个样本')
            mean, variance = x.mean(axis=0), x.var(axis=0)
            m = self.momentum
            self.mean = (1 - m) * self.mean + m * mean
            self.variance = (1 - m) * self.variance + m * variance * len(x) / (len(x) - 1)
        else:
            mean, variance = self.mean, self.variance
        return (x - mean) / np.sqrt(variance + self.eps) * self.gamma + self.beta
