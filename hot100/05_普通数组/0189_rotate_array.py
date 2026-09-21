"""189. 轮转数组
题意：原地向右轮转数组 k 步。
思路：整体翻转，再翻转前 k 项和剩余项，恢复两部分内部顺序。
时间：O(n)；空间：O(1)。
原题：https://leetcode.cn/problems/rotate-array/
"""

class Solution:
    def rotate(self, nums, k):
        if not nums:
            return
        k %= len(nums)
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        reverse(0, len(nums) - 1)
        reverse(0, k - 1)
        reverse(k, len(nums) - 1)
