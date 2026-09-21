"""21. 合并两个有序链表
题意：合并两个升序链表，复用原节点。
思路：哨兵简化头节点处理，每次接上较小的头。
时间：O(m+n)；空间：O(1)。
原题：https://leetcode.cn/problems/merge-two-sorted-lists/
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = tail = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next, list1 = list1, list1.next
            else:
                tail.next, list2 = list2, list2.next
            tail = tail.next
        tail.next = list1 or list2
        return dummy.next
