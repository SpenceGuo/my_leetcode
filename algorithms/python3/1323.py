class Solution:
    def maximum69Number (self, num: int) -> int:
        result = ""
        str_num = str(num)
        flag = True
        for s in str_num:
            if s == "6" and flag:
                result = result + "9"
                flag = False
            else:
                result = result + s
        return int(result)


x = Solution()
print(x.maximum69Number(9996669))
