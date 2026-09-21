"""正则表达式匹配
题意与思路：完整匹配，点号任意单字符，星号重复前一项；模式保证合法。滚动 DP 枚举使用零次或继续使用。
复杂度：O(mn) 时间，O(n) 空间。
来源：https://leetcode.cn/problems/regular-expression-matching/
"""

class Solution:
    def isMatch(self, s, p):
        dp = [False]*(len(p)+1)
        dp[0] = True
        for j in range(2, len(p)+1):
            if p[j-1] == '*':
                dp[j] = dp[j-2]
        for ch in s:
            new = [False]*(len(p)+1)
            for j in range(1, len(p)+1):
                if p[j-1] == '*':
                    new[j] = new[j-2] or (dp[j] and p[j-2] in (ch, '.'))
                else:
                    new[j] = dp[j-1] and p[j-1] in (ch, '.')
            dp = new
        return dp[-1]
