from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        result = []
        for i in range(1, pow(10, n)):
            result.append(i)
        return result


x = Solution()
print(x.printNumbers(1))
