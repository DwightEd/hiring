"""回文整数
题意与思路：不转字符串，只反转后半数字；末尾为零的非零数直接排除。
复杂度：O(log n) 时间，O(1) 空间。
来源：https://leetcode.cn/problems/palindrome-number/
"""

class Solution:
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half*10+x%10
            x //= 10
        return x == reversed_half or x == reversed_half//10
