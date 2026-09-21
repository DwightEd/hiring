"""146. LRU 缓存
题意：实现固定容量 LRU 缓存，get 和 put 均为常数期望时间。
思路：哈希表定位节点，双向链表维护最近使用顺序；尾部淘汰最久未用项。
时间：get/put O(1) 期望；空间：O(capacity)。
原题：https://leetcode.cn/problems/lru-cache/
"""

class _Node:
    def __init__(self, key=0, value=0):
        self.key, self.value = key, value
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity, self.nodes = capacity, {}
        self.head, self.tail = _Node(), _Node()
        self.head.next, self.tail.prev = self.tail, self.head

    def _remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def _front(self, node):
        node.prev, node.next = self.head, self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.nodes:
            return -1
        node = self.nodes[key]
        self._remove(node)
        self._front(node)
        return node.value

    def put(self, key, value):
        if key in self.nodes:
            node = self.nodes[key]
            node.value = value
            self._remove(node)
        else:
            node = self.nodes[key] = _Node(key, value)
        self._front(node)
        if len(self.nodes) > self.capacity:
            oldest = self.tail.prev
            self._remove(oldest)
            del self.nodes[oldest.key]
