from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        result = []
        nums.sort()
        index = 0
        while index<len(nums)-1:
            if nums[index] != nums[index+1]:
                result.append(nums[index])
                index += 1
            else:
                index += 2
        if (index + 1) == len(nums):
            result.append(nums[-1])
        return result


x = Solution()
print(x.singleNumbers([1,2,10,4,1,4,3,3]))
