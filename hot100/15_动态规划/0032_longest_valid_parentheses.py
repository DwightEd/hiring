"""32. 最长有效括号
题意：求最长连续合法括号子串长度。
思路：正反各扫一次；一侧括号过多时重置，平衡时更新长度。
时间：O(n)；空间：O(1)。
原题：https://leetcode.cn/problems/longest-valid-parentheses/
"""

class Solution:
    def longestValidParentheses(self, s):
        best = left = right = 0
        for ch in s:
            left += ch == '('
            right += ch == ')'
            if left == right:
                best = max(best, 2 * right)
            elif right > left:
                left = right = 0
        left = right = 0
        for ch in reversed(s):
            left += ch == '('
            right += ch == ')'
            if left == right:
                best = max(best, 2 * left)
            elif left > right:
                left = right = 0
        return best
