from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(0, len(nums)):
            if ((target - nums[i]) in nums) and (i != nums.index(target-nums[i])):
                result.append(i)
                result.append(nums.index((target - nums[i])))
                break
        return result


x = Solution()
print(x.twoSum([2, 7, 11, 15], 9))
print(x.twoSum([3, 2, 4], 6))
