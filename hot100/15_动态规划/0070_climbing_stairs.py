"""70. 爬楼梯
题意：每次登一级或两级，求到达第 n 级的方案数。
思路：Fibonacci 快速倍增，每读一个二进制位将索引翻倍。
时间：O(log n) 算术操作；大整数运算另计；空间：O(1) 个整数。
原题：https://leetcode.cn/problems/climbing-stairs/
"""

class Solution:
    def climbStairs(self, n):
        a, b = 0, 1
        for bit in bin(n + 1)[2:]:
            c = a * (2 * b - a)
            d = a * a + b * b
            a, b = (c, d) if bit == '0' else (d, c + d)
        return a
