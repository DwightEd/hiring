"""2. 两数相加
题意：两个逆序存储非负整数的链表相加，返回逆序结果。
思路：按位相加并传递 carry，两个链表结束后仍需处理最后进位。
时间：O(max(m,n))；空间：O(1)，不计输出。
原题：https://leetcode.cn/problems/add-two-numbers/
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = tail = ListNode()
        carry = 0
        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            carry, digit = divmod(total, 10)
            tail.next = ListNode(digit)
            tail = tail.next
        return dummy.next
