"""49. 字母异位词分组
题意：将小写英文字符串按字母组成分组。
思路：用 26 维计数元组作字典键，相同字母计数必然属于一组。
时间：O(S+26n)，S 为总字符数；空间：O(26n)，不计输出。
原题：https://leetcode.cn/problems/group-anagrams/
"""

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        groups = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1
            groups[tuple(count)].append(word)
        return list(groups.values())
