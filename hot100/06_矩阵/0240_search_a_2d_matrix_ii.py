"""240. 搜索二维矩阵 II
题意：在每行每列分别递增的矩阵中查找 target。
思路：从右上角出发，每步淘汰一行或一列。
时间：O(m+n)；极窄矩阵逐行二分可能更快；空间：O(1)。
原题：https://leetcode.cn/problems/search-a-2d-matrix-ii/
"""

class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            value = matrix[row][col]
            if value == target:
                return True
            if value > target:
                col -= 1
            else:
                row += 1
        return False
