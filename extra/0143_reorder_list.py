"""重排链表
题意与思路：重排为首、尾、次首、次尾；找中点、反转后半、交替合并。
复杂度：O(n) 时间，O(1) 空间。
来源：https://leetcode.cn/problems/reorder-list/
"""

class Solution:
    def reorderList(self, head):
        if not head or not head.next: return
        slow=fast=head
        while fast.next and fast.next.next:
            slow,fast=slow.next,fast.next.next
        node,slow.next=slow.next,None
        previous=None
        while node:
            following=node.next
            node.next=previous
            previous,node=node,following
        first,second=head,previous
        while second:
            a,b=first.next,second.next
            first.next=second
            second.next=a
            first,second=a,b
