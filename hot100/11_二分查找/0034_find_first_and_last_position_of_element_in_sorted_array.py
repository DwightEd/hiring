"""34. 在排序数组中查找元素的第一个和最后一个位置
题意：返回有重复升序数组中 target 的首尾下标，不存在返回 [-1,-1]。
思路：分别找第一个 >=target 与第一个 >target 的位置。
时间：O(log n)；空间：O(1)。
原题：https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/
"""

class Solution:
    def searchRange(self, nums, target):
        def boundary(strict):
            left, right = 0, len(nums)
            while left < right:
                middle = (left + right) // 2
                if nums[middle] < target or (strict and nums[middle] == target):
                    left = middle + 1
                else:
                    right = middle
            return left
        start = boundary(False)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        return [start, boundary(True) - 1]
