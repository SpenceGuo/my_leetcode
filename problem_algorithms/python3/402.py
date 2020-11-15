
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        remain = len(num) - k
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        return ''.join(stack[:remain]).lstrip('0') or '0'


x = Solution()
print(x.removeKdigits("10200", 1))
print(x.removeKdigits("10", 1))
print(x.removeKdigits("112", 1))
print(x.removeKdigits("1432219", 3))
print(x.removeKdigits("654321",3))
print('0000'.lstrip('0') or '0')
