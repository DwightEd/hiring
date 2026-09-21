"""53. 最大子数组和
题意：求非空连续子数组的最大和。
思路：以当前位置结尾的最优解只有接上前段或从本项重新开始两种。
时间：O(n)；空间：O(1)。
原题：https://leetcode.cn/problems/maximum-subarray/
"""

class Solution:
    def maxSubArray(self, nums):
        ending = best = nums[0]
        for i in range(1, len(nums)):
            ending = max(nums[i], ending + nums[i])
            best = max(best, ending)
        return best
