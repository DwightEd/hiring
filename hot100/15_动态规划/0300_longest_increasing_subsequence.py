"""300. 最长递增子序列
题意：求严格递增子序列的最长长度，子序列不要求连续。
思路：tails[length-1] 保存该长度的最小末尾，二分替换第一个 >= 当前值的位置。
时间：O(n log n)；空间：O(n)。
原题：https://leetcode.cn/problems/longest-increasing-subsequence/
"""

from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums):
        tails = []
        for value in nums:
            position = bisect_left(tails, value)
            if position == len(tails):
                tails.append(value)
            else:
                tails[position] = value
        return len(tails)
