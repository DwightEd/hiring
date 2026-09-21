"""快速幂
题意与思路：指数为负时先取倒数，二进制拆分指数；合法输入不会对零取负幂。
复杂度：O(log(abs(n)+1)) 时间，O(1) 空间。
来源：https://leetcode.cn/problems/powx-n/
"""

class Solution:
    def myPow(self, x, n):
        if n < 0:
            x, n = 1/x, -n
        result = 1.0
        while n:
            if n & 1:
                result *= x
            x *= x
            n >>= 1
        return result
