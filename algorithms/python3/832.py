from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        result = []
        for data in A:
            data.reverse()
            result.append([1 ^ a for a in data])
        return result


x = Solution()
print(x.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
