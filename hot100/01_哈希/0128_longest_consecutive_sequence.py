"""128. 最长连续序列
题意：求无序数组中连续整数序列的最长长度。
思路：只从没有前驱 x-1 的数开始扩展，每个不同数字最多被访问两次。
时间：O(n) 期望；空间：O(n)。
原题：https://leetcode.cn/problems/longest-consecutive-sequence/
"""

class Solution:
    def longestConsecutive(self, nums):
        values = set(nums)
        best = 0
        for x in values:
            if x - 1 not in values:
                end = x
                while end in values:
                    end += 1
                best = max(best, end - x)
        return best
