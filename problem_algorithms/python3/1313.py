from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0, int(len(nums)/2)):
            result.extend([nums[2*i + 1]]*nums[2*i])
        return result


x = Solution()
print(x.decompressRLElist([1,2,3,4]))