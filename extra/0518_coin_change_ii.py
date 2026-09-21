"""零钱兑换组合数
题意与思路：面额互异正数且可无限使用；先遍历硬币，再顺序遍历金额，避免计算排列。
复杂度：O(amount·种类数) 时间，O(amount) 空间。
来源：https://leetcode.cn/problems/coin-change-ii/
"""

class Solution:
    def change(self,amount,coins):
        dp=[1]+[0]*amount
        for coin in coins:
            for value in range(coin,amount+1): dp[value]+=dp[value-coin]
        return dp[-1]
