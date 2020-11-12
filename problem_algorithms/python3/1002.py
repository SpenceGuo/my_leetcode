from typing import List
from collections import Counter


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if not A:
            return []
        final = []
        letters = []
        result = list(range(26))

        for i in range(97, 123):
            letters.append(chr(i))

        for i in range(0, 26):
            result[i] = float('inf')

        for word in A:
            for i in range(0, 26):
                if result[i] > word.count(letters[i]):
                    result[i] = word.count(letters[i])

        for i in range(0, 26):
            if result[i] < float('inf') and result[i] >0:
                for j in range(0, result[i]):
                    final.append(chr(i+97))
        return final


test = ["cool", "lock", "cook"]
x = Solution()
print(x.commonChars(test))

