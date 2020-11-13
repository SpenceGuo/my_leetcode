import math


class Solution:
    def maximum(self, a: int, b: int) -> int:
        return int((math.fabs(a - b) + a + b) / 2)
