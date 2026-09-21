"""1143. 最长公共子序列
题意：求两个字符串最长公共子序列长度。
思路：滚动 DP 保存上方、左方和左上方状态，用短串作为列。
时间：O(mn)；空间：O(min(m,n))。
原题：https://leetcode.cn/problems/longest-common-subsequence/
"""

class Solution:
    def longestCommonSubsequence(self, text1, text2):
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        dp = [0] * (len(text2) + 1)
        for a in text1:
            diagonal = 0
            for j, b in enumerate(text2, 1):
                old = dp[j]
                dp[j] = diagonal + 1 if a == b else max(dp[j], dp[j - 1])
                diagonal = old
        return dp[-1]
