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

    def solveNQueensReadable(self, n):
        """用显式的行、列和对角线集合枚举所有合法棋盘。"""
        answer = []
        path = []
        used_columns = set()
        used_left_diagonals = set()
        used_right_diagonals = set()

        def backtrack(row):
            if row == n:
                board = [
                    '.' * column + 'Q' + '.' * (n - column - 1)
                    for column in path
                ]
                answer.append(board)
                return

            for column in range(n):
                # 同一条对角线上的格子具有相同的 row-column 或 row+column。
                left_diagonal = row - column
                right_diagonal = row + column
                if (
                    column in used_columns
                    or left_diagonal in used_left_diagonals
                    or right_diagonal in used_right_diagonals
                ):
                    continue

                path.append(column)
                used_columns.add(column)
                used_left_diagonals.add(left_diagonal)
                used_right_diagonals.add(right_diagonal)

                backtrack(row + 1)

                path.pop()
                used_columns.remove(column)
                used_left_diagonals.remove(left_diagonal)
                used_right_diagonals.remove(right_diagonal)

        backtrack(0)
        return answer


def main():
    n = 4
    solution = Solution()
    result = solution.solveNQueensReadable(n)
    for board in result:
        for row in board:
            print(row)
        print()


if __name__ == "__main__":
    main()
