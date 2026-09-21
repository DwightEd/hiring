"""K-means 聚类
分类：机器学习
题意：x 为 N×D，1<=k<=N，返回分配标签和中心；seed 固定初始化。
思路：Lloyd 交替最近中心分配与均值更新；空簇保持旧中心，返回前重新分配。
复杂度：O(iter·N·k·D) 时间，O(Nk+kD) 空间。
来源性质：通用算法手撕练习；具体公司出处仅以 companies/README.md 的映射为准。
"""

import numpy as np

def kmeans(x, k, max_iter=100, tol=1e-6, seed=0):
    x = np.asarray(x, dtype=float)
    if not 1 <= k <= len(x):
        raise ValueError('k 越界')
    centers = x[np.random.default_rng(seed).choice(len(x), k, replace=False)].copy()
    def assign():
        distances = np.sum(x*x, axis=1)[:, None] + np.sum(centers*centers, axis=1)[None, :] - 2*x@centers.T
        return distances.argmin(axis=1)
    for _ in range(max_iter):
        labels, new = assign(), centers.copy()
        for cluster in range(k):
            members = x[labels == cluster]
            if len(members):
                new[cluster] = members.mean(axis=0)
        difference = np.linalg.norm(new - centers)
        centers = new
        if difference <= tol:
            break
    return assign(), centers
