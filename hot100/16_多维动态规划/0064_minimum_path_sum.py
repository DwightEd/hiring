"""64. 最小路径和
题意：非负网格只能向右或下，求最小路径和；不修改网格。
思路：一维 DP 覆盖前为上方状态，覆盖后为左方状态。
时间：O(mn)；空间：O(n)，n 为列数。
原题：https://leetcode.cn/problems/minimum-path-sum/
"""

class Solution:
    def minPathSum(self, grid):
        dp = [float('inf')] * len(grid[0])
        dp[0] = 0
        for row in grid:
            for j, value in enumerate(row):
                dp[j] = value + min(dp[j], dp[j - 1] if j else float('inf'))
        return dp[-1]
