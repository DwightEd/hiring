"""23. 合并 K 个升序链表
题意：合并 k 条升序链表，复用节点。
思路：最小堆仅保留每条链的当前头，链编号用于打破相同值的比较。
时间：O(N log(k+1))，N 为总节点数；空间：O(k)。
原题：https://leetcode.cn/problems/merge-k-sorted-lists/
"""

from heapq import heapify, heappop, heappush

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

class Solution:
    def mergeKLists(self, lists):
        heap = [(node.val, i, node) for i, node in enumerate(lists) if node]
        heapify(heap)
        dummy = tail = ListNode()
        while heap:
            _, i, node = heappop(heap)
            tail.next, tail = node, node
            if node.next:
                heappush(heap, (node.next.val, i, node.next))
        return dummy.next
