"""155. 最小栈
题意：实现支持常数时间最小值查询的栈。
思路：每个栈项同时保存当时的前缀最小值。
时间：每次操作 O(1)；空间：O(n)。
原题：https://leetcode.cn/problems/min-stack/
"""

class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        minimum = min(val, self.stack[-1][1]) if self.stack else val
        self.stack.append((val, minimum))

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]
