class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = ""
        word_dic = {}
        for i in range(1, 10):
            word_dic[str(i)] = chr(96 + i)
        for j in range(10, 27):
            word_dic[str(j) + "#"] = chr(96 + j)

        m, n = 0, 2
        while(m < len(s)):
            if m > (len(s)-3) or s[n] != '#':
                result = result + word_dic[s[m]]
                m += 1
                n += 1
            else:
                index = s[m] + s[m+1] + s[m+2]
                result = result + word_dic[index]
                m += 3
                n += 3
        return result


s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
x = Solution()
print(x.freqAlphabets(s))

