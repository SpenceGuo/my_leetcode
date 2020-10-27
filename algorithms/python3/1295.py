from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in range(0, len(nums)):
            # 思路就是转化为字符串
            if nums[i].__str__().__len__() % 2 == 0:
                count += 1
        return count

