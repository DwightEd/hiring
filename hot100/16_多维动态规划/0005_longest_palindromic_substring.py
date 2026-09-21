"""5. 最长回文子串
题意：返回最长回文子串，多个答案时返回最先出现的一个。
思路：Manacher 使用镜像半径，已知最右回文范围内不用从零扩展。
时间：O(n)；空间：O(n)。
原题：https://leetcode.cn/problems/longest-palindromic-substring/
"""

class Solution:
    def longestPalindrome(self, s):
        # None 为分隔符，不会与任何实际字符冲突。
        transformed = [None]
        for ch in s:
            transformed.extend((ch, None))
        radius = [0] * len(transformed)
        center = right = best_center = best_radius = 0
        for i in range(len(transformed)):
            if i < right:
                radius[i] = min(right - i, radius[2 * center - i])
            while i-radius[i]-1 >= 0 and i+radius[i]+1 < len(transformed) and transformed[i-radius[i]-1] == transformed[i+radius[i]+1]:
                radius[i] += 1
            if i + radius[i] > right:
                center, right = i, i + radius[i]
            if radius[i] > best_radius:
                best_center, best_radius = i, radius[i]
        start = (best_center - best_radius) // 2
        return s[start:start + best_radius]
