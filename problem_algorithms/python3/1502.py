from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        flag = True
        arr.sort()
        for i in range(1, len(arr)-1):
            if (arr[i-1]-arr[i]) != (arr[i]-arr[i+1]):
                flag = False
                break
        return flag
