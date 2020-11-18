from typing import List
import math


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        sums = 0
        for i in range(n):
            sums += mat[i][i]
        for j in range(n):
            sums += mat[n-j-1][j]
        if n%2 == 1:
            sums -= mat[math.floor(n/2)][math.floor(n/2)]
        return sums


x = Solution()
print(x.diagonalSum([[1,2,3],
            [4,5,6],
            [7,8,9]]))