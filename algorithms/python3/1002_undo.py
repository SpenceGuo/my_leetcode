from typing import List
from collections import Counter


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        result = []
        test = A[0]
        for i in range(0, len(test)):
            flag = True
            for j in range(1, len(A)):
                if A[j].count(test[i]) == 0:
                    flag = False
            if flag:
                result.append(test[i])
        return result


x = Solution()
print(x.commonChars(["cool","lock","cook"]))
