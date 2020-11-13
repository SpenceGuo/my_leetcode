class Solution:
    def divisorGame(self, N: int) -> bool:
        flag = True
        if N % 2 == 1:
            flag = False
        return flag