"""3. 无重复字符的最长子串
题意：求不含重复字符的最长连续子串长度。
思路：记录字符上次位置；左边界只能右移，不能退回旧窗口。
时间：O(n) 期望；空间：O(字符集大小)。
原题：https://leetcode.cn/problems/longest-substring-without-repeating-characters/
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        last, left, best = {}, 0, 0
        for right, ch in enumerate(s):
            left = max(left, last.get(ch, -1) + 1)
            last[ch] = right
            best = max(best, right - left + 1)
        return best
