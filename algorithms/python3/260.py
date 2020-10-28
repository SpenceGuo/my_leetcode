from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0, len(nums)):
            if nums.count(nums[i]) == 1:
                result.append(nums[i])
        return result


"""
from collections import Counter
class Solution:
    def singleNumber(self, nums: int) -> List[int]:
        hashmap = Counter(nums)
        return [x for x in hashmap if hashmap[x] == 1]
"""
