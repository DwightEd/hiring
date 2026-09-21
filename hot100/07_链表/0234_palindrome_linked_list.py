"""234. 回文链表
题意：判断链表是否回文，并恢复原链表。
思路：快慢指针找前半段末尾，反转后半段比较，最后再次反转恢复。
时间：O(n)；空间：O(1)。
原题：https://leetcode.cn/problems/palindrome-linked-list/
"""

class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        def reverse(node):
            previous = None
            while node:
                following = node.next
                node.next = previous
                previous, node = node, following
            return previous
        slow = fast = head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        second = reverse(slow.next)
        a, b, result = head, second, True
        while b:
            if a.val != b.val:
                result = False
            a, b = a.next, b.next
        slow.next = reverse(second)
        return result
