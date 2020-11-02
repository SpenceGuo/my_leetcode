from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a = max(nums)
        nums.remove(a)
        b = max(nums)
        return (a-1)*(b-1)


x = Solution()
print(x.maxProduct([1,1,1,1]))
