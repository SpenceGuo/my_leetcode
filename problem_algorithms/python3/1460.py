from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        flag = True
        arr.sort()
        target.sort()

        for i in range(0, len(arr)):
            if arr[i] != target[i]:
                flag = False
        return flag


x = Solution()
print(x.canBeEqual([1, 2, 2, 3], [1, 1, 2, 3]))
