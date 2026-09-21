"""原地等概率洗牌
分类：随机算法
题意：原地打乱数组，返回同一数组；seed 便于复现实验。
思路：从后往前，位置 i 与 [0,i] 均匀随机位置交换。
复杂度：O(n) 时间，O(1) 辅助空间。
来源性质：通用算法手撕练习；具体公司出处仅以 companies/README.md 的映射为准。
"""

from random import Random

def shuffle(values, seed=None):
    rng = Random(seed)
    for i in range(len(values) - 1, 0, -1):
        j = rng.randrange(i + 1)
        values[i], values[j] = values[j], values[i]
    return values
