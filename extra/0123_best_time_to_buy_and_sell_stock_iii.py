"""股票最多两次交易
题意与思路：维护第一次买卖和第二次买卖四个状态。
复杂度：O(n) 时间，O(1) 空间。
来源：https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/
"""

class Solution:
    def maxProfit(self, prices):
        buy1 = buy2 = float('-inf')
        sell1 = sell2 = 0
        for price in prices:
            buy1 = max(buy1,-price)
            sell1 = max(sell1,buy1+price)
            buy2 = max(buy2,sell1-price)
            sell2 = max(sell2,buy2+price)
        return sell2
