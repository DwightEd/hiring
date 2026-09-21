"""141. 环形链表
题意：判断链表是否有环。
思路：快指针每轮两步，慢指针一步；有环必相遇。
时间：O(n)；空间：O(1)。
原题：https://leetcode.cn/problems/linked-list-cycle/
"""

class Solution:
    def hasCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                return True
        return False
