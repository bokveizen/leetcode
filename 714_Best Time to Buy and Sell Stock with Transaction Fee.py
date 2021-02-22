# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) < 2:
            return 0
        dp = [[0, 0] for _ in prices]
        for i in range(len(prices)):
            if i == 0:
                dp[i] = [0, -prices[0]]
            else:
                dp[i] = [max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee),
                         max(dp[i - 1][1], dp[i - 1][0] - prices[i])]
        return dp[-1][0]


# greedy
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        buy = prices[0] + fee
        profit = 0
        for i in range(1, n):
            if prices[i] + fee < buy:
                buy = prices[i] + fee
            elif prices[i] > buy:
                profit += prices[i] - buy
                buy = prices[i]
        return profit
