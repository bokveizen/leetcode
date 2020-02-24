# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
class Solution0:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        dp = [[0, 0] for _ in prices]
        for i in range(len(prices)):
            if i == 0:
                dp[i] = [0, -prices[0]]
            else:
                dp[i] = [max(dp[i - 1][0], dp[i - 1][1] + prices[i]),
                         max(dp[i - 1][1], -prices[i])]
        return dp[-1][0]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        dp = [0, -prices[0]]
        for i in range(1, len(prices)):
            if dp[1] + prices[i] > dp[0]:
                dp[0] = dp[1] + prices[i]
            if -prices[i] > dp[1]:
                dp[1] = -prices[i]
        return dp[0]
