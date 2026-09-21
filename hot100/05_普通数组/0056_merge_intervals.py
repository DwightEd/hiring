"""56. 合并区间
题意：合并相交闭区间，返回互不相交的区间。
思路：按左端排序后，只可能与最后一个已合并区间相交。
时间：O(n log n)；空间：O(n)。
原题：https://leetcode.cn/problems/merge-intervals/
"""

class Solution:
    def merge(self, intervals):
        result = []
        for left, right in sorted(intervals):
            if result and left <= result[-1][1]:
                result[-1][1] = max(result[-1][1], right)
            else:
                result.append([left, right])
        return result
