"""215. 数组中的第K个最大元素
题意：找第 k 大元素，重复值计入排名，修改输入。
思路：随机枢轴三路快选，一次排除小于、等于或大于枢轴的整段。
时间：O(n) 期望，最坏 O(n²)；不是最坏线性保证；空间：O(1)。
原题：https://leetcode.cn/problems/kth-largest-element-in-an-array/
"""

from random import randrange

class Solution:
    def findKthLargest(self, nums, k):
        target, left, right = len(nums) - k, 0, len(nums) - 1
        while left <= right:
            pivot = nums[randrange(left, right + 1)]
            low, index, high = left, left, right
            while index <= high:
                if nums[index] < pivot:
                    nums[low], nums[index] = nums[index], nums[low]
                    low += 1
                    index += 1
                elif nums[index] > pivot:
                    nums[index], nums[high] = nums[high], nums[index]
                    high -= 1
                else:
                    index += 1
            if target < low:
                right = low - 1
            elif target > high:
                left = high + 1
            else:
                return nums[target]
