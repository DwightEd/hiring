"""移掉 K 位数字
题意与思路：删除恰好 k 位使非负数最小，单调栈贪心优先删除较大的前位。
复杂度：O(n) 时间和空间。
来源：https://leetcode.cn/problems/remove-k-digits/
"""

class Solution:
    def removeKdigits(self,num,k):
        stack=[]
        for ch in num:
            while k and stack and stack[-1]>ch:
                stack.pop();k-=1
            stack.append(ch)
        if k: del stack[-k:]
        return ''.join(stack).lstrip('0') or '0'
