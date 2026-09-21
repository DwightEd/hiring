"""76. 最小覆盖子串
题意：求 s 中包含 t 所有字符及重复次数的最短子串。
思路：缺失总字符数为零后收缩左端，直到不再满足覆盖。
时间：O(n+m) 期望；空间：O(字符集大小)。
原题：https://leetcode.cn/problems/minimum-window-substring/
"""

from collections import Counter

class Solution:
    def minWindow(self, s, t):
        if not t:
            return ''
        need = Counter(t)
        missing, left = len(t), 0
        best_left, best_size = 0, len(s) + 1
        for right, ch in enumerate(s):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1
            while missing == 0:
                if right - left + 1 < best_size:
                    best_left, best_size = left, right - left + 1
                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1
        return '' if best_size > len(s) else s[best_left:best_left + best_size]
