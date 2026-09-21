"""41. 缺失的第一个正数
题意：原地求未出现的最小正整数。
思路：把范围 1..n 的值 x 放在 x-1 位置；重复值不能交换，否则死循环。
时间：O(n)，每次成功交换至少归位一个数；空间：O(1)。
原题：https://leetcode.cn/problems/first-missing-positive/
"""

class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                destination = nums[i] - 1
                nums[i], nums[destination] = nums[destination], nums[i]
        for i, value in enumerate(nums):
            if value != i + 1:
                return i + 1
        return n + 1
