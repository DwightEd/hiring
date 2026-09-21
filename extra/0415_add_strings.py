"""大数加法
题意与思路：不整体转 int，逆序逐位加法处理进位。
复杂度：O(m+n) 时间，O(max(m,n)) 输出空间。
来源：https://leetcode.cn/problems/add-strings/
"""

class Solution:
    def addStrings(self,num1,num2):
        i,j,carry=len(num1)-1,len(num2)-1,0
        digits=[]
        while i>=0 or j>=0 or carry:
            value=carry
            if i>=0: value+=ord(num1[i])-48;i-=1
            if j>=0: value+=ord(num2[j])-48;j-=1
            carry,digit=divmod(value,10)
            digits.append(str(digit))
        return ''.join(reversed(digits))
