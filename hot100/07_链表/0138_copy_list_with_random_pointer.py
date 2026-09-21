"""138. 随机链表的复制
题意：深拷贝包含 next 与 random 指针的链表。
思路：将副本插在原节点后，用原 random.next 定位副本，再拆开两条链。
时间：O(n)；空间：O(1)，不计输出。
原题：https://leetcode.cn/problems/copy-list-with-random-pointer/
"""

class Node:
    def __init__(self, x, next=None, random=None):
        self.val, self.next, self.random = x, next, random

class Solution:
    def copyRandomList(self, head):
        if head is None:
            return None
        current = head
        while current:
            current.next = Node(current.val, current.next)
            current = current.next.next
        current = head
        while current:
            current.next.random = current.random.next if current.random else None
            current = current.next.next
        copy_head, current = head.next, head
        while current:
            copy = current.next
            current.next = copy.next
            copy.next = copy.next.next if copy.next else None
            current = current.next
        return copy_head
