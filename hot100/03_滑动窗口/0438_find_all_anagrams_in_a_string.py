"""438. 找到字符串中所有字母异位词
题意：返回 s 中所有与 p 字母计数相同的窗口起点；字符为小写英文。
思路：固定长度滑窗维护计数，26 维比较是常数开销。
时间：O(n+m)，常数 26；空间：O(1)，不计输出。
原题：https://leetcode.cn/problems/find-all-anagrams-in-a-string/
"""

class Solution:
    def findAnagrams(self, s, p):
        need, have = [0] * 26, [0] * 26
        for ch in p:
            need[ord(ch) - 97] += 1
        answer, width = [], len(p)
        for i, ch in enumerate(s):
            have[ord(ch) - 97] += 1
            if i >= width:
                have[ord(s[i - width]) - 97] -= 1
            if i >= width - 1 and have == need:
                answer.append(i - width + 1)
        return answer
