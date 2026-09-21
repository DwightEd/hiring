"""73. 矩阵置零
题意：原地把包含零的整行整列清零。
思路：第一行和第一列存标记；单独记住它们原本是否含零。
时间：O(mn)；空间：O(1)。
原题：https://leetcode.cn/problems/set-matrix-zeroes/
"""

class Solution:
    def setZeroes(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        first_row = any(x == 0 for x in matrix[0])
        first_col = any(matrix[i][0] == 0 for i in range(rows))
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if first_row:
            for j in range(cols):
                matrix[0][j] = 0
        if first_col:
            for i in range(rows):
                matrix[i][0] = 0
