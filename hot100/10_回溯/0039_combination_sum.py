"""39. 组合总和
题意：用互异正整数 candidates 可重复取数，枚举和为 target 的无序组合。
思路：按非降顺序取数，避免排列重复；排序后剩余和不足便剪枝。
时间：O(n^(T/m+1)) 粗上界，n 为候选数，m 为最小候选；空间：O(T/m+n)，不计输出。
原题：https://leetcode.cn/problems/combination-sum/
"""

class Solution:
    def combinationSum(self, candidates, target):
        values, answer, path = sorted(candidates), [], []
        def dfs(start, remaining):
            if remaining == 0:
                answer.append(path.copy())
                return
            for i in range(start, len(values)):
                if values[i] > remaining:
                    break
                path.append(values[i])
                dfs(i, remaining - values[i])
                path.pop()
        dfs(0, target)
        return answer
