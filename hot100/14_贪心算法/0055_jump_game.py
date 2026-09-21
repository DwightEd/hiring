"""55. 跳跃游戏
题意：nums[i] 是最大跳跃长度，判断能否到达末尾。
思路：扫描可达前缀并扩展最远位置，一旦当前位置越界就失败。
时间：O(n)；空间：O(1)。
原题：https://leetcode.cn/problems/jump-game/
"""

class Solution:
    def canJump(self, nums):
        farthest = 0
        for i, step in enumerate(nums):
            if i > farthest:
                return False
            farthest = max(farthest, i + step)
        return True
