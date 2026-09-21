"""153. 寻找旋转排序数组中的最小值
题意：求互异元素旋转升序数组的最小值。
思路：中点大于右端则最小值在右半，否则最小值不越过中点。
时间：O(log n)；空间：O(1)。
原题：https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/
"""

class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            middle = (left + right) // 2
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle
        return nums[left]
