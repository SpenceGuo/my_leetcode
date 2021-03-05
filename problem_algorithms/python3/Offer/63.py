from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 暴力求解
        # profit = 0
        # if len(prices) <= 1:
        #     return profit
        # for i in range(0, len(prices)-1):
        #     for j in range(i+1, len(prices)):
        #         if prices[j] - prices[i] > profit:
        #             profit = prices[j] - prices[i]
        # return profit

        # 动态规划求解
        cost, profit = float("+inf"), 0
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit
