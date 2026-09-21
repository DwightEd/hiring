"""45. 跳跃游戏 II
题意：保证可到达末尾，求最少跳跃次数。
思路：把一次跳跃可到达的区间看作 BFS 一层，到本层边界时增加步数。
时间：O(n)；空间：O(1)。
原题：https://leetcode.cn/problems/jump-game-ii/
"""

class Solution:
    def jump(self, nums):
        end = farthest = steps = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == end:
                steps += 1
                end = farthest
        return steps
