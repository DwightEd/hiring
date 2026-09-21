"""35. 搜索插入位置
题意：在升序互异数组中返回 target 的位置或插入位置。
思路：左闭右开区间二分寻找第一个大于等于 target 的位置。
时间：O(log n)；空间：O(1)。
原题：https://leetcode.cn/problems/search-insert-position/
"""

class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle
        return left
