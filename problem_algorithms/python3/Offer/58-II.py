class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        head = s[:n]
        tail = s[n:]
        return tail+head