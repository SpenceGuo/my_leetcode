from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        i = 1
        result = 0
        # i = len(arr) 时，就是整个数组
        while i <= len(arr):
            for j in range(0, len(arr)-i+1):
                result += sum(arr[j:j+i])
            i += 2
        return result


x = Solution()
print(x.sumOddLengthSubarrays([1,4,2,5,3]))