from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        if n == 0:
            return []
        if n == 1:
            return [0]
        if n % 2 == 1:
            result.append(0)
            for i in range(1, int((n-1)/2 + 1)):
                result.append(i)
                result.append(i * (-1))
        else:
            for i in range(1, int(n/2 + 1)):
                result.append(i)
                result.append(i * (-1))
        return result


x = Solution()
print(x.sumZero(5))
