from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)<=1:
            return []
        dic = {}
        result = []
        for i in range(len(nums)):
            dic[nums[i]] = nums[i]
        for j in range(int(target/2) + 1):
            if j in dic and (target-j) in dic:
                result.append(j)
                result.append(target-j)
                break
        return result
