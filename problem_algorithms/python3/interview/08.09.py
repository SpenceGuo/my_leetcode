from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        if n < 1:
            return []

        def dfs(left, right, temp=''):
            if left > right:
                return
            if left == 0 and right == 0:
                result.append(temp)
                return
            if left > 0:
                dfs(left-1, right, temp+'(')
            if right > 0:
                dfs(left, right-1, temp+')')
        dfs(n, n)
        return result


x = Solution()
print(x.generateParenthesis(2))
