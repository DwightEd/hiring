"""739. 每日温度
题意：返回每一天等到更暖温度需几天，无更暖日则为零。
思路：栈内下标对应温度递减，遇到更暖日就为被弹出的日期结算。
时间：O(n)；空间：O(n)。
原题：https://leetcode.cn/problems/daily-temperatures/
"""

class Solution:
    def dailyTemperatures(self, temperatures):
        stack, answer = [], [0] * len(temperatures)
        for i, value in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < value:
                old = stack.pop()
                answer[old] = i - old
            stack.append(i)
        return answer
