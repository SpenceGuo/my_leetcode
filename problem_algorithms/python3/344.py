from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        temp = 0
        if len(s) % 2 == 1:
            for i in range(0, int((len(s)-1)/2)):
                temp = s[i]
                s[i] = s[(i+1)*(-1)]
                s[(i + 1) * (-1)] = temp
        else:
            for i in range(0, int((len(s))/2)):
                temp = s[i]
                s[i] = s[(i+1)*(-1)]
                s[(i + 1) * (-1)] = temp
