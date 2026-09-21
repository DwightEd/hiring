"""最大数
题意与思路：把非负整数排列成拼接最大值，用 a+b 与 b+a 决定两数顺序。
复杂度：O(n log n·L) 时间，O(nL) 空间。
来源：https://leetcode.cn/problems/largest-number/
"""

from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        def compare(a,b):
            return (a+b < b+a)-(a+b > b+a)
        parts=sorted(map(str,nums),key=cmp_to_key(compare))
        return '0' if parts[0]=='0' else ''.join(parts)
