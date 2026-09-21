"""51. N 皇后
题意：枚举 n 皇后互不攻击的棋盘。
思路：逐行放皇后，用位掩码排除列及两类对角线；仅枚举可放位置。
时间：O(n!+S·n²) 上界，S 为解数；空间：O(n)，不计输出。
原题：https://leetcode.cn/problems/n-queens/
"""

class Solution:
    def solveNQueens(self, n):
        mask, answer, path = (1 << n) - 1, [], []
        def dfs(columns, left_diagonal, right_diagonal):
            if columns == mask:
                answer.append(['.' * col + 'Q' + '.' * (n-col-1) for col in path])
                return
            available = mask & ~(columns | left_diagonal | right_diagonal)
            while available:
                bit = available & -available
                available -= bit
                path.append(bit.bit_length() - 1)
                dfs(columns | bit, ((left_diagonal | bit) << 1) & mask, (right_diagonal | bit) >> 1)
                path.pop()
        dfs(0, 0, 0)
        return answer
