"""118. 杨辉三角
题意：生成杨辉三角的前 numRows 行。
思路：每行首尾为一，中间项来自上一行相邻两项之和。
时间：O(n²)，与输出规模一致；空间：O(n²)，含输出。
原题：https://leetcode.cn/problems/pascals-triangle/
"""

class Solution:
    def generate(self, numRows):
        answer = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = answer[-1][j - 1] + answer[-1][j]
            answer.append(row)
        return answer
