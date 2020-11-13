from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        if not nums:
            return result
        result.append([nums[0]])
        for i in range(1, len(nums)):
            result += [x + [nums[i]] for x in result]
        return result

x = Solution()
print(x.subsets([1,2,3]))
