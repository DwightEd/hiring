"""347. 前 K 个高频元素
题意：返回出现次数最多的 k 个数，答案集合唯一。
思路：频率最多为 n，使用频次桶从高到低收集，避免全排序。
时间：O(n) 期望；空间：O(n)。
原题：https://leetcode.cn/problems/top-k-frequent-elements/
"""

from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        buckets = [[] for _ in range(len(nums) + 1)]
        for value, frequency in Counter(nums).items():
            buckets[frequency].append(value)
        answer = []
        for frequency in range(len(nums), 0, -1):
            for value in buckets[frequency]:
                answer.append(value)
                if len(answer) == k:
                    return answer
