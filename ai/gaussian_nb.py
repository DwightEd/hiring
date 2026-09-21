"""高斯朴素贝叶斯
分类：机器学习
题意：训练每类先验、各维均值与方差，按条件独立假设分类。
思路：在 log 域累加概率，方差加平滑，避免连乘下溢与零方差。
复杂度：此按类切片实现训练 O(CN+ND)，预测 O(MCD)。
来源性质：通用算法手撕练习；具体公司出处仅以 companies/README.md 的映射为准。
"""

import numpy as np

class GaussianNB:
    def fit(self, x, y, eps=1e-9):
        x, y = np.asarray(x, dtype=float), np.asarray(y)
        self.classes, counts = np.unique(y, return_counts=True)
        self.log_prior = np.log(counts / len(y))
        self.mean = np.array([x[y == c].mean(axis=0) for c in self.classes])
        self.var = np.array([x[y == c].var(axis=0) + eps for c in self.classes])
        return self

    def predict(self, x):
        scores = self.log_prior - 0.5 * np.sum(np.log(2*np.pi*self.var) + (np.asarray(x)[:, None, :] - self.mean)**2 / self.var, axis=-1)
        return self.classes[scores.argmax(axis=1)]
