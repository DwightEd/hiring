"""169. 多数元素
题意：保证有一个值出现超过一半次数，返回它。
思路：Boyer-Moore 不同值两两抵消，多数值最终一定存活。
时间：O(n)；空间：O(1)。
原题：https://leetcode.cn/problems/majority-element/
"""

class Solution:
    def majorityElement(self, nums):
        candidate, votes = None, 0
        for value in nums:
            if votes == 0:
                candidate = value
            votes += 1 if value == candidate else -1
        return candidate
