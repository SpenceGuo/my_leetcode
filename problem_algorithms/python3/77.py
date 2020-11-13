from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        if not nums:
            return result
        for i in range(0, len(nums)):
            result += [x+[nums[i]] for x in result]
        return result
