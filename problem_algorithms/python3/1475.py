from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = []
        for i in range(0, len(prices)-1):
            result.append(prices[i])
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    result.pop(-1)
                    result.append(prices[i] - prices[j])
                    break
        result.append(prices[-1])
        return result
