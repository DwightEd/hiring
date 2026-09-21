"""22. 括号生成
题意：枚举 n 对括号形成的全部合法字符串。
思路：左括号最多 n 个，右括号数始终不能超过左括号数。
时间：O(n·C_n)，C_n 为第 n 个 Catalan 数；空间：O(n)，不计输出。
原题：https://leetcode.cn/problems/generate-parentheses/
"""

class Solution:
    def generateParenthesis(self, n):
        answer, path = [], []
        def dfs(left, right):
            if right == n:
                answer.append(''.join(path))
                return
            if left < n:
                path.append('(')
                dfs(left + 1, right)
                path.pop()
            if right < left:
                path.append(')')
                dfs(left, right + 1)
                path.pop()
        dfs(0, 0)
        return answer
