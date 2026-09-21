"""763. 划分字母区间
题意：切分字符串，使每种字母只出现在一段中，并尽量多分段。
思路：当前段必须覆盖已见字符的最后出现位置，到达最远尾端才能切开。
时间：O(n)；空间：O(字符集大小)，不计输出。
原题：https://leetcode.cn/problems/partition-labels/
"""

class Solution:
    def partitionLabels(self, s):
        last = {ch: i for i, ch in enumerate(s)}
        start = end = 0
        result = []
        for i, ch in enumerate(s):
            end = max(end, last[ch])
            if i == end:
                result.append(i - start + 1)
                start = i + 1
        return result
