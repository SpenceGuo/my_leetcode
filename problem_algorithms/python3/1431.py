from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        flag = [False] * len(candies)
        for i in range(0, len(candies)):
            if candies[i] + extraCandies >= max(candies):
                flag[i] = True
        return flag


print([False] * len([2,3,5,1,3]))