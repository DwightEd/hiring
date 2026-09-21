"""20. 有效的括号
题意：判断仅包含三类括号的字符串是否合法匹配。
思路：左括号入栈，右括号必须与栈顶配对。
时间：O(n)；空间：O(n)。
原题：https://leetcode.cn/problems/valid-parentheses/
"""

class Solution:
    def isValid(self, s):
        pairs, stack = {')':'(', ']':'[', '}':'{'}, []
        for ch in s:
            if ch not in pairs:
                stack.append(ch)
            elif not stack or stack.pop() != pairs[ch]:
                return False
        return not stack
