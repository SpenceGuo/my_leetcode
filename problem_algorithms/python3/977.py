from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        result = A
        B = [x*x for x in result]
        B.sort()
        return B