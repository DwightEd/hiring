"""74. 搜索二维矩阵
题意：在按行展开后整体升序的矩阵中查找 target。
思路：将一维下标通过 divmod 映射到行列，直接二分。
时间：O(log(mn))；空间：O(1)。
原题：https://leetcode.cn/problems/search-a-2d-matrix/
"""

class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        cols = len(matrix[0])
        left, right = 0, len(matrix) * cols
        while left < right:
            middle = (left + right) // 2
            row, col = divmod(middle, cols)
            if matrix[row][col] < target:
                left = middle + 1
            else:
                right = middle
        return left < len(matrix) * cols and matrix[left // cols][left % cols] == target
