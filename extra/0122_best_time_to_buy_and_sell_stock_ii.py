"""股票无限次交易
题意与思路：同时最多持有一股；将所有相邻上涨收益累加。
复杂度：O(n) 时间，O(1) 空间。
来源：https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/
"""

class Solution:
    def maxProfit(self, prices):
        return sum(max(0, prices[i]-prices[i-1]) for i in range(1,len(prices)))
