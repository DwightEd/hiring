"""25. K 个一组翻转链表
题意：每 k 个节点为一组反转，不足 k 个的尾组保持原样。
思路：先确认组尾存在，反转到组后节点为止，再连接组前驱。
时间：O(n)；空间：O(1)。
原题：https://leetcode.cn/problems/reverse-nodes-in-k-group/
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

class Solution:
    def reverseKGroup(self, head, k):
        dummy = before = ListNode(0, head)
        while True:
            end = before
            for _ in range(k):
                end = end.next
                if end is None:
                    return dummy.next
            after = end.next
            old_first = current = before.next
            previous = after
            while current is not after:
                following = current.next
                current.next = previous
                previous, current = current, following
            before.next = end
            before = old_first
