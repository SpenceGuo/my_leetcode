from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        flag = False
        nums.sort()
        zero_count = nums.count(0)
        for i in range(zero_count,4):
            if nums[i] == nums[i+1]: return False
        if (nums[-1]-nums[zero_count])<5:
            flag = True
        return flag