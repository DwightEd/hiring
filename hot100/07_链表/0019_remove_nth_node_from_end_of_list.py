"""19. 删除链表的倒数第 N 个结点
题意：删除链表倒数第 n 个节点，n 合法。
思路：两指针相距 n 个节点，让慢指针最终停在待删节点的前驱。
时间：O(L)，L 为链表长度；空间：O(1)。
原题：https://leetcode.cn/problems/remove-nth-node-from-end-of-list/
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        slow = fast = dummy
        for _ in range(n):
            fast = fast.next
        while fast.next:
            slow, fast = slow.next, fast.next
        slow.next = slow.next.next
        return dummy.next
