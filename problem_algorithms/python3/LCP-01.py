from typing import List


class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        count = 0
        for i in range(0, 3):
            if guess[i] == answer[i]: count += 1
        return count