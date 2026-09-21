"""翻转单词顺序
题意与思路：按空白拆词，逆序连接，并去除多余空格。
复杂度：O(n) 时间和空间。
来源：https://leetcode.cn/problems/reverse-words-in-a-string/
"""

class Solution:
    def reverseWords(self, s):
        return ' '.join(reversed(s.split()))
