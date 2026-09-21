"""279. 完全平方数
题意：求最少几个完全平方数之和等于正整数 n。
思路：四平方和定理：去除因子 4 后为 7 mod 8 则需 4；再检查 1 和 2，其余为 3。
时间：O(sqrt(n)) 算术操作；空间：O(1)。
原题：https://leetcode.cn/problems/perfect-squares/
"""

from math import isqrt

class Solution:
    def numSquares(self, n):
        if isqrt(n) ** 2 == n:
            return 1
        reduced = n
        while reduced % 4 == 0:
            reduced //= 4
        if reduced % 8 == 7:
            return 4
        for a in range(1, isqrt(n) + 1):
            remainder = n - a * a
            if isqrt(remainder) ** 2 == remainder:
                return 2
        return 3
