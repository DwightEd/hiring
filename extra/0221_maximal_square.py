"""最大正方形
题意与思路：字符 0/1 网格，dp 为以当前格为右下角的最大边长，依赖左、上、左上最小值。
复杂度：O(mn) 时间，O(n) 空间。
来源：https://leetcode.cn/problems/maximal-square/
"""

class Solution:
    def maximalSquare(self, matrix):
        if not matrix: return 0
        dp=[0]*(len(matrix[0])+1)
        best=0
        for row in matrix:
            diagonal=0
            for j,ch in enumerate(row,1):
                old=dp[j]
                dp[j]=1+min(dp[j],dp[j-1],diagonal) if ch=='1' else 0
                diagonal=old
                best=max(best,dp[j])
        return best*best
