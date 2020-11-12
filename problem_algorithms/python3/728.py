from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        if left>right:
            return result

        for i in range(left, right+1):
            if "0" in str(i):
                continue
            else:
                flag = True
                for num in str(i):
                    if i % int(num) != 0:
                        flag = False
                if flag:
                    result.append(i)
        return result


x = Solution()
print(x.selfDividingNumbers(1, 22))
