from typing import List


class Solution:
    def minCount(self, coins: List[int]) -> int:
        # 第一种方法：
        # count = 0
        # for i in range(0, len(coins)):
        #     while coins[i] >= 2:
        #         coins[i] -= 2
        #         count += 1
        #     while coins[i] == 1:
        #         coins[i] -= 1
        #         count += 1
        # return count
        return sum([(x+1)//2 for x in coins])
