from typing import List


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        result = [(i, j) for i in range(R) for j in range(C)]
        result.sort(key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))
        return result