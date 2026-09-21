"""股票交易手续费
题意与思路：无限交易，每次卖出收一次手续费；维护持股和空仓状态。
复杂度：O(n) 时间，O(1) 空间。
来源：https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
"""

class Solution:
    def maxProfit(self,prices,fee):
        hold,cash=float('-inf'),0
        for price in prices:
            hold,cash=max(hold,cash-price),max(cash,hold+price-fee)
        return cash
