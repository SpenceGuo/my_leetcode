from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        """
            1. dp问题: dp[i] = dp[i-1] * 10 + dp[i-1][-1] +/- K.
            其中dp[i-1][-1]代表dp[i-1]的个位数, +/- K代表对K的加减.
        """
        dp = range(10)
        for _ in range(n - 1):
            _dp = set()
            for x in dp:
                for y in [x % 10 + k, x % 10 - k]:
                    if x and 0 <= y <= 9:
                        _dp.add(x * 10 + y)
            dp = _dp

        return list(dp)


x = Solution()
print(x.numsSameConsecDiff(3, 7))