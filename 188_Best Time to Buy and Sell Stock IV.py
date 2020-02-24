# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) < 2 or k == 0:
            return 0
        if 2 * k >= len(prices):
            return sum(profit for profit in [prices[i + 1] - prices[i] for i in range(len(prices) - 1)] if profit > 0)
        dp = [[[0, -prices[0]] for _ in range(k + 1)] for _ in prices]
        for i in range(1, len(prices)):
            dp[i][0] = dp[i - 1][0]
            for buying_times in range(1, k + 1):
                dp[i][buying_times] = [max(dp[i - 1][buying_times][0], dp[i - 1][buying_times][1] + prices[i]),
                                       max(dp[i - 1][buying_times][1], dp[i - 1][buying_times - 1][0] - prices[i])]
        return dp[-1][k][0]
