from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        st_up = []
        st_down = []
        for i in range(len(A)):
            while len(st_down)>0 and A[i]>st_down[-1]:
                st_down.pop()
            while len(st_up)>0 and A[i]<st_up[-1]:
                st_up.pop()
            st_down.append(A[i])
            st_up.append(A[i])
        if len(st_up)==len(A) or len(st_down)==len(A):
            return True
        return False