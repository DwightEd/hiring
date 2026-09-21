"""字符串相乘
题意与思路：非负十进制数不能整体转 int；按竖式把每对数位贡献加到结果数组。
复杂度：O(mn) 时间，O(m+n) 空间。
来源：https://leetcode.cn/problems/multiply-strings/
"""

class Solution:
    def multiply(self, num1, num2):
        digits = [0]*(len(num1)+len(num2))
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                total = (ord(num1[i])-48)*(ord(num2[j])-48)+digits[i+j+1]
                digits[i+j+1] = total%10
                digits[i+j] += total//10
        return ''.join(map(str,digits)).lstrip('0') or '0'
