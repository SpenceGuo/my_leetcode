class Solution:
    def sortString(self, s: str) -> str:
        result = ""
        letter_list = []
        for letter in s:
            letter_list.append(letter)
        letter_list.sort()

        return result


x = Solution()
print(x.sortString("baaaabbbcccc"))
