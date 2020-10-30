import numpy as np
from typing import List


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        count = 0
        result = np.zeros([n, m], int)
        for data in indices:
            row_index = data[0]
            collum_index = data[1]
            result[row_index, :] + 1


a = np.zeros([2, 3], int)
print(a[1, :] + 1)
print(a)
