"""字符串转换整数
题意与思路：跳过前导空格，读取可选符号与连续数字，截断到有符号 32 位范围。
复杂度：O(n) 时间，O(1) 空间。
来源：https://leetcode.cn/problems/string-to-integer-atoi/
"""

class Solution:
    def myAtoi(self, s):
        i, sign, value = 0, 1, 0
        while i < len(s) and s[i] == ' ':
            i += 1
        if i < len(s) and s[i] in '+-':
            sign = -1 if s[i] == '-' else 1
            i += 1
        limit = 2**31 if sign < 0 else 2**31-1
        while i < len(s) and '0' <= s[i] <= '9':
            digit = ord(s[i])-48
            if value > (limit-digit)//10:
                return sign*limit
            value = value*10+digit
            i += 1
        return sign*value
