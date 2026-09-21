"""比较版本号
题意与思路：按点分隔的各段数值比较，忽略前导零与末尾零段；不把超长段转 int。
复杂度：O(m+n) 时间和空间。
来源：https://leetcode.cn/problems/compare-version-numbers/
"""

from itertools import zip_longest

class Solution:
    def compareVersion(self, version1, version2):
        for a,b in zip_longest(version1.split('.'),version2.split('.'),fillvalue='0'):
            a,b=a.lstrip('0') or '0',b.lstrip('0') or '0'
            if len(a)!=len(b): return 1 if len(a)>len(b) else -1
            if a!=b: return 1 if a>b else -1
        return 0
