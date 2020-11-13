from typing import List
import numpy as np


class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        lucly = []
        matrix = np.array(matrix)
        m = len(matrix)
        n = len(matrix[0])
        num = min(m, n)
        for i in range(0, m):
            for j in range(0, n):
                if matrix[i][j] == min(matrix[i]) and matrix[i][j] == max(matrix[:, j]):
                    lucly.append(int(matrix[i][j]))
        return lucly



# matrix = [[3,7,8],[9,11,13],[15,16,17]]
# row_count = len(matrix)
# coliumn_count = len(matrix[0])
# matrix = np.array(matrix)
# print(matrix)
# print(len(matrix))
# print(matrix[0])
# print(matrix[:, 0])

x = Solution()
print(x.luckyNumbers([[7,8],[1,2]]))

