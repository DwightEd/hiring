"""24. 两两交换链表中的节点
题意：每两个相邻节点交换位置，不能仅交换节点值。
思路：保存每组前驱，重连前驱、第二个、第一个和下一组。
时间：O(n)；空间：O(1)。
原题：https://leetcode.cn/problems/swap-nodes-in-pairs/
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

class Solution:
    def swapPairs(self, head):
        dummy = previous = ListNode(0, head)
        while previous.next and previous.next.next:
            first, second = previous.next, previous.next.next
            first.next = second.next
            second.next = first
            previous.next = second
            previous = first
        return dummy.next
