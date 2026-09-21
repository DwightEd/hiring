"""72. 编辑距离
题意：用插入、删除或替换把一个字符串变成另一个，求最少操作数。
思路：每格依赖左、上、左上，滚动数组压缩空间。
时间：O(mn)；空间：O(min(m,n))。
原题：https://leetcode.cn/problems/edit-distance/
"""

class Solution:
    def minDistance(self, word1, word2):
        if len(word1) < len(word2):
            word1, word2 = word2, word1
        dp = list(range(len(word2) + 1))
        for i, a in enumerate(word1, 1):
            diagonal, dp[0] = dp[0], i
            for j, b in enumerate(word2, 1):
                old = dp[j]
                dp[j] = diagonal if a == b else 1 + min(diagonal, dp[j], dp[j - 1])
                diagonal = old
        return dp[-1]
