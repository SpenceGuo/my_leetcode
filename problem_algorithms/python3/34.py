from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        for i in range(0, len(nums)):
            if nums[i] == target:
                result[0] = i
                for j in range(i, len(nums)):
                    if nums[j] == target:
                        result[1] = j
                break
        return result
