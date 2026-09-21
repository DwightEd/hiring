"""股票冷冻期
题意与思路：卖出后一天不能买入，维护持股、今天卖出、空仓休息三个状态。
复杂度：O(n) 时间，O(1) 空间。
来源：https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/
"""

class Solution:
    def maxProfit(self, prices):
        hold,sold,rest=float('-inf'),float('-inf'),0
        for price in prices:
            hold,sold,rest=max(hold,rest-price),hold+price,max(rest,sold)
        return max(rest,sold)
