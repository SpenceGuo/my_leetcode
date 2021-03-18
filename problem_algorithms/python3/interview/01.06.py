class Solution:
    def compressString(self, S: str) -> str:
        if len(S) < 2: return S
        result = ''
        length = len(S)
        count = 1
        for i in range(length - 1):
            if S[i] != S[i+1]:
                result = result + str(S[i]) + str(count)
                count = 0
            count += 1
        result = result + str(S[-1]) + str(count)
        if len(result) < len(S):
            return result
        return S

x = Solution()
print(x.compressString("aabccccdd"))
