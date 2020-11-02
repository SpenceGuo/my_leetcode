class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(" ", "%20")


x = Solution()
print(x.replaceSpace("We are happy."))
