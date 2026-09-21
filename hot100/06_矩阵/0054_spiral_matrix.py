"""54. 螺旋矩阵
题意：按顺时针螺旋顺序遍历矩阵。
思路：每圈维护上、下、左、右边界；最后一行或一列不能重复输出。
时间：O(mn)；空间：O(1)，不计输出。
原题：https://leetcode.cn/problems/spiral-matrix/
"""

class Solution:
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        answer = []
        while top <= bottom and left <= right:
            for j in range(left, right + 1):
                answer.append(matrix[top][j])
            top += 1
            for i in range(top, bottom + 1):
                answer.append(matrix[i][right])
            right -= 1
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    answer.append(matrix[bottom][j])
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    answer.append(matrix[i][left])
                left += 1
        return answer
