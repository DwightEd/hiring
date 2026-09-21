"""11. 盛最多水的容器
题意：选两条竖线，求其与横轴围成的最大容积。
思路：宽度缩小时只有提高短边才可能改善面积，因此移动较短边。
时间：O(n)；空间：O(1)。
原题：https://leetcode.cn/problems/container-with-most-water/
"""

class Solution:
    def maxArea(self, height):
        left, right, best = 0, len(height) - 1, 0
        while left < right:
            best = max(best, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return best
