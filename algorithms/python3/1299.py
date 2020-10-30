from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # 使用list的内置函数 max() 找出后面的最大值
        result = []
        rest = []
        for j in range(0, len(arr)):
            rest.append(arr[j])
        for i in range(0, len(arr) - 1):
            rest.remove(arr[i])
            result.append(max(rest))
        result.append(-1)
        return result


x = Solution()
print(x.replaceElements([17,18,5,4,6,1]))
