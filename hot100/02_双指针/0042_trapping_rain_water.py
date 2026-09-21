"""42. 接雨水
题意：求柱状高度数组能接住的雨水总量。
思路：左右最高边界中较矮的一边已确定该位置水位，可立即结算。
时间：O(n)；空间：O(1)。
原题：https://leetcode.cn/problems/trapping-rain-water/
"""

class Solution:
    def trap(self, height):
        left, right = 0, len(height) - 1
        left_max = right_max = water = 0
        while left <= right:
            if left_max <= right_max:
                left_max = max(left_max, height[left])
                water += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                water += right_max - height[right]
                right -= 1
        return water
