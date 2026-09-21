"""基本计算器
题意与思路：支持整数、空格、加减与括号，含一元负号；栈保存括号外的总和与符号。
复杂度：O(n) 时间，O(n) 空间。
来源：https://leetcode.cn/problems/basic-calculator/
"""

class Solution:
    def calculate(self, s):
        stack=[]
        total,number,sign=0,0,1
        for ch in s:
            if ch.isdigit(): number=number*10+int(ch)
            elif ch in '+-':
                total+=sign*number
                number,sign=0,1 if ch=='+' else -1
            elif ch=='(':
                stack.append((total,sign))
                total,sign=0,1
            elif ch==')':
                total+=sign*number
                outside,outer_sign=stack.pop()
                total=outside+outer_sign*total
                number=0
        return total+sign*number
