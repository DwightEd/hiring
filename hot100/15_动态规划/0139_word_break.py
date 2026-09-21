"""139. 单词拆分
题意：判断字符串是否能由字典中非空单词拼接，单词可重复。
思路：字典构建 Trie，从每个可达切分点沿 Trie 扩展，避免反复切片。
时间：O(S+n·L)，S 为词典字符数，L 为最长词长；空间：O(S+n)。
原题：https://leetcode.cn/problems/word-break/
"""

class Solution:
    def wordBreak(self, s, wordDict):
        root = {}
        for word in wordDict:
            node = root
            for ch in word:
                node = node.setdefault(ch, {})
            node[None] = True
        reachable = [False] * (len(s) + 1)
        reachable[0] = True
        for start in range(len(s)):
            if not reachable[start]:
                continue
            node = root
            for end in range(start, len(s)):
                if s[end] not in node:
                    break
                node = node[s[end]]
                if None in node:
                    reachable[end + 1] = True
        return reachable[-1]
