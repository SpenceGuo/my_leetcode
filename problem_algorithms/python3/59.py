from typing import List
import numpy as np


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = np.zeros((n, n), dtype=int)
        target = n * n
        left, right, top, bottom = 0, n-1, 0, n-1
        index = 1
        while index<=target:
            for i in range(left, right+1):
                result[top][i] = index
                index = index + 1
            top = top + 1
            for i in range(top, bottom+1):
                result[i][right] = index
                index = index + 1
            right = right - 1
            for i in range(right, left-1, -1):
                result[bottom][i] = index
                index = index + 1
            bottom = bottom - 1
            for i in range(bottom, top-1, -1):
                result[i][left] = index
                index = index + 1
            left = left + 1
        return result.tolist()


x = Solution()
print(x.generateMatrix(3))
