from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) > 1:
            for i in range(len(nums)-1):
                if nums[i] == nums[i+1]:
                    return nums[i]
        return None
