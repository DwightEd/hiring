"""131. 分割回文串
题意：枚举把字符串切成若干回文子串的所有方案。
思路：先用 DP 预计算回文区间，再按可行右端点回溯。
时间：O(n²+n·2^n)，含输出；空间：O(n²)，不计输出。
原题：https://leetcode.cn/problems/palindrome-partitioning/
"""

class Solution:
    def partition(self, s):
        n = len(s)
        palindrome = [[False] * n for _ in range(n)]
        for left in range(n - 1, -1, -1):
            for right in range(left, n):
                palindrome[left][right] = s[left] == s[right] and (right-left < 2 or palindrome[left+1][right-1])
        result, path = [], []
        def dfs(start):
            if start == n:
                result.append(path.copy())
                return
            for end in range(start, n):
                if palindrome[start][end]:
                    path.append(s[start:end+1])
                    dfs(end + 1)
                    path.pop()
        dfs(0)
        return result
