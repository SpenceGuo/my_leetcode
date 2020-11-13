class Solution:
    def generateTheString(self, n: int) -> str:
        if n <= 0:
            return ""
        result = ""
        if n % 2 == 1:
            for i in range(0, n):
                result = result + 'a'
        else:
            result = result + 'b'
            for i in range(0, n - 1):
                result = result + 'a'
        return result