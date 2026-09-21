"""160. 相交链表
题意：返回两个无环链表相交的节点，按对象身份而非值判断。
思路：两指针走完自身后换到对方头部，路径长度相同，最终同点或同为空。
时间：O(m+n)；空间：O(1)。
原题：https://leetcode.cn/problems/intersection-of-two-linked-lists/
"""

class Solution:
    def getIntersectionNode(self, headA, headB):
        a, b = headA, headB
        while a is not b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
