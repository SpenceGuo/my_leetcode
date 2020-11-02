class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        result = bin(x ^ y).__str__().replace("0b", "")
        for i in range(0, result.__len__()):
            if result[i] == "1":
                count += 1
        return count


x = Solution()
print(x.hammingDistance(1, 4))
