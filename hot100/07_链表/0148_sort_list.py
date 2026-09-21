"""148. 排序链表
题意：对链表升序排序，复用节点。
思路：自底向上归并，段长逐轮翻倍；避免递归栈，实现常数辅助空间。
时间：O(n log n)；空间：O(1)。
原题：https://leetcode.cn/problems/sort-list/
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

class Solution:
    def sortList(self, head):
        n, node = 0, head
        while node:
            n, node = n + 1, node.next
        def split(node, size):
            if not node:
                return None
            for _ in range(size - 1):
                if not node.next:
                    break
                node = node.next
            following, node.next = node.next, None
            return following
        dummy, size = ListNode(0, head), 1
        while size < n:
            tail, current = dummy, dummy.next
            while current:
                left = current
                right = split(left, size)
                current = split(right, size)
                while left and right:
                    if left.val <= right.val:
                        tail.next, left = left, left.next
                    else:
                        tail.next, right = right, right.next
                    tail = tail.next
                tail.next = left or right
                while tail.next:
                    tail = tail.next
            size *= 2
        return dummy.next
