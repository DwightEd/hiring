"""1. 两数之和
题意：返回数组中和为 target 的两个不同位置。
思路：边扫描边存已见数的下标，先查补数再加入当前数，避免重复使用自身。
时间：O(n) 期望；空间：O(n)。
原题：https://leetcode.cn/problems/two-sum/
"""

class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, value in enumerate(nums):
            if target - value in seen:
                return [seen[target - value], i]
            seen[value] = i
