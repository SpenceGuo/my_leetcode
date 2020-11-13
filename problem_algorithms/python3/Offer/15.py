
class Solution:
    def hammingWeight(self, n: int) -> int:
        return str(bin(n)).count('1')


x = Solution()
print(x.hammingWeight(11))
