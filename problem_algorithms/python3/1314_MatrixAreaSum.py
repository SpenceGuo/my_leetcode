from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        rows, columns = len(mat), len(mat[0])
        dp = [[0]*columns for _ in range(rows)]
        for i in range(0, rows):
            for j in range(0, columns):
                a, b = self.getEdges(i, j, K, rows, columns)
                for z in range(a[0], a[1]+1):
                    for y in range(b[0], b[1]+1):
                        dp[i][j] += mat[z][y]
        return dp

    def getEdges(self, i, j, K, rows, columns):
        a, b = [0, 0], [0, 0]
        a[0] = 0 if i-K < 0 else i-K
        a[1] = rows-1 if i+K>rows-1 else i+K
        b[0] = 0 if j-K<0 else j-K
        b[1] = columns-1 if j+K>columns-1 else j+K
        return a, b


x = Solution()
print(x.matrixBlockSum([[1,2,3],[4,5,6],[7,8,9]], 1))
print(x.getEdges(0,0,1,3,3))

