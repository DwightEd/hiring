"""206. 反转链表
题意：原地反转单链表。
思路：每次保存后继，再把当前 next 指向已反转的前缀。
时间：O(n)；空间：O(1)。
原题：https://leetcode.cn/problems/reverse-linked-list/
"""

class Solution:
    def reverseList(self, head):
        previous = None
        while head:
            following = head.next
            head.next = previous
            previous, head = head, following
        return previous
