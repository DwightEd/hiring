"""208. 实现 Trie (前缀树)
题意：实现字符串插入、整词查找和前缀查找。
思路：每条边对应一个字符；终止标记区别整词与前缀。
时间：每次 O(L) 期望；空间：O(总字符数)。
原题：https://leetcode.cn/problems/implement-trie-prefix-tree/
"""

class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node[None] = True

    def _find(self, text):
        node = self.root
        for ch in text:
            if ch not in node:
                return None
            node = node[ch]
        return node

    def search(self, word):
        node = self._find(word)
        return node is not None and None in node

    def startsWith(self, prefix):
        return self._find(prefix) is not None
