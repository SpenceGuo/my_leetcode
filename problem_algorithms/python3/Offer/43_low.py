class Solution:
    def countDigitOne(self, n: int) -> int:
        result = []
        count = 0
        for i in range(1, n+1):
            count += str(i).count('1')
            result.append(count)
        return result[n-1]


x = Solution()
print(x.countDigitOne(1000000))
