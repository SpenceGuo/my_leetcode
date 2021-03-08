from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return i+1