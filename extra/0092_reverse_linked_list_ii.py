"""指定区间反转链表
题意与思路：1-based 区间 left..right 原地反转；不断把后继搬到区间最前面。
复杂度：O(n) 时间，O(1) 空间。
来源：https://leetcode.cn/problems/reverse-linked-list-ii/
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

class Solution:
    def reverseBetween(self, head, left, right):
        dummy = before = ListNode(0, head)
        for _ in range(left-1):
            before = before.next
        tail = before.next
        for _ in range(right-left):
            moved = tail.next
            tail.next = moved.next
            moved.next = before.next
            before.next = moved
        return dummy.next
