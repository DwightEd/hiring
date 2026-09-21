"""322. 零钱兑换
题意：无限使用正面额硬币，求凑出 amount 的最少枚数，不可行返回 -1。
思路：dp[x] 从每个合法最后硬币转移，amount+1 表示不可达。
时间：O(amount·种类数)，标准伪多项式 DP；空间：O(amount)。
原题：https://leetcode.cn/problems/coin-change/
"""

class Solution:
    def coinChange(self, coins, amount):
        dp = [0] + [amount + 1] * amount
        for total in range(1, amount + 1):
            for coin in coins:
                if coin <= total:
                    dp[total] = min(dp[total], dp[total - coin] + 1)
        return dp[amount] if dp[amount] <= amount else -1
