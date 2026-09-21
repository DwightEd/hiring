"""双栈实现队列
题意与思路：输入栈只负责追加，输出栈为空时一次搬运全部元素。
复杂度：操作均摊 O(1)，O(n) 空间。
来源：https://leetcode.cn/problems/implement-queue-using-stacks/
"""

class MyQueue:
    def __init__(self): self.incoming,self.outgoing=[],[]
    def push(self,x): self.incoming.append(x)
    def _move(self):
        if not self.outgoing:
            while self.incoming: self.outgoing.append(self.incoming.pop())
    def pop(self):
        self._move()
        return self.outgoing.pop()
    def peek(self):
        self._move()
        return self.outgoing[-1]
    def empty(self): return not self.incoming and not self.outgoing
