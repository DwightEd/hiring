"""142. 环形链表 II
题意：返回链表入环节点，无环返回 None。
思路：相遇后一个指针回头部，两指针同步一步，再相遇就是入口。
时间：O(n)；空间：O(1)。
原题：https://leetcode.cn/problems/linked-list-cycle-ii/
"""

class Solution:
    def detectCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                seeker = head
                while seeker is not slow:
                    seeker, slow = seeker.next, slow.next
                return seeker
        return None
