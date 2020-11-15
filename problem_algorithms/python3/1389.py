from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(index)):
            target.insert(index[i], nums[i])
        return target



x = Solution()
print(x.createTargetArray([1,2,3,4,5], [5,4,3,2,1]))
