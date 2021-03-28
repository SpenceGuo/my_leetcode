# import numpy as np
# grid = [
#     [3, 0, 8, 4],
#     [2, 4, 5, 7],
#     [9, 2, 6, 3],
#     [0, 3, 1, 0]
# ]
# temp = np.array(grid)
# print([temp[:, i-1:i].flatten().tolist() for i in range(1, 5)])
# print([max(grid[:1]) for _ in range(4)])

import numpy as np
from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        if len(grid)==1 and len(grid[0]) == 1:
            return 0
        rows, columns = len(grid), len(grid[0])
        count = 0
        max_h = []
        max_v = []
        temp = np.array(grid)
        for h in grid:
            max_h.append(max(h))
        for v in [temp[:, i-1:i].flatten().tolist() for i in range(1, columns+1)]:
            max_v.append(max(v))
        for i in range(0, rows):
            for j in range(0, columns):
                if grid[i][j]<max_h[i] and grid[i][j]<max_v[j]:
                    count += min(max_h[i], max_v[j]) - grid[i][j]
        return count
