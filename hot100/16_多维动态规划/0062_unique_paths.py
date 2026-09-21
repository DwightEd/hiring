"""62. 不同路径
题意：m×n 网格只能向右或向下，求左上到右下路径数。
思路：总步数 m+n-2 中选择 m-1 次向下，用整数乘除逐项算组合数。
时间：O(min(m,n)) 算术操作，大整数成本另计；空间：O(1) 个整数。
原题：https://leetcode.cn/problems/unique-paths/
"""

class Solution:
    def uniquePaths(self, m, n):
        total, choose, answer = m + n - 2, min(m - 1, n - 1), 1
        for i in range(1, choose + 1):
            answer = answer * (total - choose + i) // i
        return answer
