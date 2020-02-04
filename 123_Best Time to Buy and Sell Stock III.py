# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        dp = [[[0, 0] for _ in range(3)] for _ in prices]
        dp[0] = [[0, -prices[0]], [0, -prices[0]], [0, -prices[0]]]
        for i in range(1, len(prices)):
            dp[i] = [dp[i - 1][0],
                     [max(dp[i - 1][1][0], dp[i - 1][1][1] + prices[i]),
                      max(dp[i - 1][1][1], - prices[i])],
                     [max(dp[i - 1][2][0], dp[i - 1][2][1] + prices[i]),
                      max(dp[i - 1][2][1], dp[i - 1][1][0] - prices[i])]]
        return dp[-1][2][0]
