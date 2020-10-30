class Solution:
    def toLowerCase(self, str: str) -> str:
        result = ""
        for i in range(0, str.__len__()):
            if ord(str[i]) in range(65, 91):
                result = result + chr(ord(str[i]) + 32)
            else:
                result = result + str[i]
        return result


x = Solution()
print(x.toLowerCase("SDReee"))
