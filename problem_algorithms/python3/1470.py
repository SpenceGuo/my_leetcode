from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l1 = []
        l2 = []
        result = []
        for i in range(0, n):
            l1.append(nums[i])
        for j in range(n, 2*n):
            l2.append(nums[j])
        for k in range(0, n):
            result.append(l1[k])
            result.append(l2[k])
        return result


x = Solution()
print(x.shuffle([1,2,3,4,4,3,2,1], 4))
