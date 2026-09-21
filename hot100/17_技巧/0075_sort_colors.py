"""75. 颜色分类
题意：原地将仅含 0、1、2 的数组排序。
思路：荷兰国旗分区：左侧全零、右侧全二，中间扫描；换入右侧未知值时不前进。
时间：O(n)；空间：O(1)。
原题：https://leetcode.cn/problems/sort-colors/
"""

class Solution:
    def sortColors(self, nums):
        left, index, right = 0, 0, len(nums) - 1
        while index <= right:
            if nums[index] == 0:
                nums[left], nums[index] = nums[index], nums[left]
                left += 1
                index += 1
            elif nums[index] == 2:
                nums[index], nums[right] = nums[right], nums[index]
                right -= 1
            else:
                index += 1
