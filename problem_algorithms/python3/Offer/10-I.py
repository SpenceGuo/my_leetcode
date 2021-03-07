"""
1. 递归法（会超出时间限制）,最好的解法应该是使用线性规划算法

class Solution:
    def fib(self, n: int) -> int:
        def rec(m):
            if m <= 1:
                return m
            return rec(m-1) + rec(m-2)
        return rec(n)

2. 带记忆数组的递归法
class Solution:
    def fib(self, n: int) -> int:
        def rec(m):
            if m <= 1:
                return m
            return rec(m-1) + rec(m-2)
        return rec(n)

3. 动态规划：程序如下
"""


class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a % 1000000007


x = Solution()
print(x.fib(4))
