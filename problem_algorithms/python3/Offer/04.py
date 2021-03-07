from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix)<1 or len(matrix[0])<1:
            return False
        for i in range(len(matrix)):
            if matrix[i][0] <= target and matrix[i][-1] >= target:
                for j in range(len(matrix[i])):
                    if target == matrix[i][j]:
                        return True
        return False


x = Solution()
print(x.findNumberIn2DArray([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))
print(x.findNumberIn2DArray([], 0))
