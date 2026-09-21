"""84. 柱状图中最大的矩形
题意：求柱状图内最大矩形面积。
思路：单调栈在较矮柱出现时确定旧柱右边界，弹出后的栈顶确定左边界。
时间：O(n)；空间：O(n)。
原题：https://leetcode.cn/problems/largest-rectangle-in-histogram/
"""

class Solution:
    def largestRectangleArea(self, heights):
        stack, best = [], 0
        for i in range(len(heights) + 1):
            height = heights[i] if i < len(heights) else 0
            while stack and heights[stack[-1]] > height:
                middle = stack.pop()
                left = stack[-1] if stack else -1
                best = max(best, heights[middle] * (i - left - 1))
            stack.append(i)
        return best
