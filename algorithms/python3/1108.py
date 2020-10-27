from typing import List


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")


x = Solution()
print(x.defangIPaddr("\"1.1.1.1\""))
