class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        if x == 0: return 0
        if n < 0:
            x = 1/x
            n = -n
        for _ in range(n):
            result *= x
        return result
