"""48. 旋转图像
题意：原地把 n×n 方阵顺时针旋转 90 度。
思路：先沿主对角线转置，再把每一行翻转。
时间：O(n²)；空间：O(1)。
原题：https://leetcode.cn/problems/rotate-image/
"""

class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()
