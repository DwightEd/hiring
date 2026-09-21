"""31. 下一个排列
题意：原地改成字典序紧邻的下一个排列，无更大排列则变最小排列。
思路：找最右上升点，与右侧最小更大值交换，再反转递减后缀。
时间：O(n)；空间：O(1)。
原题：https://leetcode.cn/problems/next-permutation/
"""

class Solution:
    def nextPermutation(self, nums):
        pivot = len(nums) - 2
        while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:
            pivot -= 1
        if pivot >= 0:
            successor = len(nums) - 1
            while nums[successor] <= nums[pivot]:
                successor -= 1
            nums[pivot], nums[successor] = nums[successor], nums[pivot]
        left, right = pivot + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
