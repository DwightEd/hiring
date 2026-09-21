"""121. 买卖股票的最佳时机
题意：最多买卖一次股票，买入必须早于卖出。
思路：保存历史最低买入价，用当前价结算卖出收益。
时间：O(n)；空间：O(1)。
原题：https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/
"""

class Solution:
    def maxProfit(self, prices):
        minimum, best = float('inf'), 0
        for price in prices:
            minimum = min(minimum, price)
            best = max(best, price - minimum)
        return best
