"""560. 和为 K 的子数组
题意：统计和恰好为 k 的连续子数组数，数组可含负数。
思路：当前前缀和为 s 时，之前每个 s-k 都对应一个答案；先查再计数。
时间：O(n) 期望；空间：O(n)。
原题：https://leetcode.cn/problems/subarray-sum-equals-k/
"""

class Solution:
    def subarraySum(self, nums, k):
        counts = {0: 1}  # 空前缀让从下标 0 开始的子数组也被计入。
        prefix = result = 0
        for value in nums:
            prefix += value
            result += counts.get(prefix - k, 0)
            counts[prefix] = counts.get(prefix, 0) + 1
        return result
