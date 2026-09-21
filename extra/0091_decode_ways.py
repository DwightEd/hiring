"""数字串解码计数
题意与思路：1..26 对应字母，零不能单独解码；滚动 DP 考虑一位和两位结尾。
复杂度：O(n) 时间，O(1) 空间。
来源：https://leetcode.cn/problems/decode-ways/
"""

class Solution:
    def numDecodings(self, s):
        before, previous = 1, 1
        for i, ch in enumerate(s):
            current = previous if ch != '0' else 0
            if i and 10 <= int(s[i-1:i+1]) <= 26:
                current += before
            before, previous = previous, current
        return previous if s else 0
