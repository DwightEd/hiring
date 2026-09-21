"""198. 打家劫舍
题意：从非负收益房屋中选互不相邻的项，求最大收益。
思路：当前最优为不偷本家或偷本家加前两家最优，滚动保存两个状态。
时间：O(n)；空间：O(1)。
原题：https://leetcode.cn/problems/house-robber/
"""

class Solution:
    def rob(self, nums):
        before, previous = 0, 0
        for value in nums:
            before, previous = previous, max(previous, before + value)
        return previous
