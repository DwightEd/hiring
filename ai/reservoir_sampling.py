"""蓄水池抽样
分类：随机算法
题意：从长度未知的可迭代流中等概率抽取 k 项；若不足 k 项则返回全部。
思路：第 i 项以 k/i 概率进入，随机替换池内一个位置。
复杂度：O(n) 时间，O(k) 空间。
来源性质：通用算法手撕练习；具体公司出处仅以 companies/README.md 的映射为准。
"""

from random import Random

def reservoir_sample(stream, k, seed=None):
    if k < 0:
        raise ValueError('k 不能为负')
    rng, result = Random(seed), []
    for index, value in enumerate(stream):
        if index < k:
            result.append(value)
        else:
            replace = rng.randrange(index + 1)
            if replace < k:
                result[replace] = value
    return result
