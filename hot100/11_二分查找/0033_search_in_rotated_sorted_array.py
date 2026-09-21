"""33. 搜索旋转排序数组
题意：在互异元素的旋转升序数组中查找 target。
思路：每次至少一半有序，判断 target 是否落在有序半区。
时间：O(log n)；空间：O(1)。
原题：https://leetcode.cn/problems/search-in-rotated-sorted-array/
"""

class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            if nums[left] <= nums[middle]:
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            elif nums[middle] < target <= nums[right]:
                left = middle + 1
            else:
                right = middle - 1
        return -1
