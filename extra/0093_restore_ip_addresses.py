"""复原 IPv4 地址
题意与思路：数字串分成四段，每段 0..255 且无前导零；按剩余长度剪枝。
复杂度：输出敏感，最多枚举 3^4 个分段；O(n) 输出空间。
来源：https://leetcode.cn/problems/restore-ip-addresses/
"""

class Solution:
    def restoreIpAddresses(self, s):
        result, path = [], []
        def dfs(start):
            remaining = 4-len(path)
            if not remaining <= len(s)-start <= 3*remaining:
                return
            if remaining == 0:
                result.append('.'.join(path))
                return
            for end in range(start+1, min(start+3, len(s))+1):
                part = s[start:end]
                if len(part)>1 and part[0]=='0' or int(part)>255:
                    break
                path.append(part)
                dfs(end)
                path.pop()
        dfs(0)
        return result
