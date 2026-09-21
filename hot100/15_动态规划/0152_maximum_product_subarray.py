"""152. 乘积最大子数组
题意：求非空连续子数组的最大乘积。
思路：负数能把最小值变最大，同时保存当前结尾的最大和最小乘积。
时间：O(n)；空间：O(1)。
原题：https://leetcode.cn/problems/maximum-product-subarray/
"""

class Solution:
    def maxProduct(self, nums):
        high = low = best = nums[0]
        for i in range(1, len(nums)):
            value = nums[i]
            high, low = max(value, high * value, low * value), min(value, high * value, low * value)
            best = max(best, high)
        return best
