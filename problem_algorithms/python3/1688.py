class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n == 1:
            return 0

        def get_count(m):
            if m // 2 == 1 and m % 2 == 0:
                return 1
            elif m % 2 == 0:
                return get_count(m // 2) + m // 2
            else:
                return get_count(m // 2 + 1) + m // 2

        return get_count(n)