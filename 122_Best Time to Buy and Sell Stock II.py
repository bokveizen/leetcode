# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(profit for profit in [prices[i + 1] - prices[i] for i in range(len(prices) - 1)] if profit > 0)
