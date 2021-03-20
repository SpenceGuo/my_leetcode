from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) <= 1:
            return sum(grid[0])
        elif len(grid[0]) <= 1:
            return sum([i[0] for i in grid])
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for a in range(1, m):
            dp[a][0] = dp[a-1][0] + grid[a][0]
        for b in range(1, n):
            dp[0][b] = dp[0][b-1] + grid[0][b]
        for a in range(1, m):
            for b in range(1, n):
                dp[a][b] = min(dp[a-1][b], dp[a][b-1]) + grid[a][b]
        return dp[m-1][n-1]


x = Solution()
print(x.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
