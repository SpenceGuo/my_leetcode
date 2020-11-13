class Solution:
    def sumNums(self, n: int) -> int:
        def sums(n):
            if n == 1:
                return 1
            return n + sums(n - 1)
        result = sums(n)
        return result


x = Solution()
print(x.sumNums(9))
