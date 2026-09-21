"""整数平方根
题意与思路：二分寻找平方不超过 x 的最大整数，不用浮点。
复杂度：O(log(x+1)) 算术操作，O(1) 空间。
来源：https://leetcode.cn/problems/sqrtx/
"""

class Solution:
    def mySqrt(self, x):
        left, right = 0, x+1
        while left+1 < right:
            middle = (left+right)//2
            if middle*middle <= x:
                left = middle
            else:
                right = middle
        return left
