class Solution:
    def smallerNumbersThanCurrent(self, nums):
        result = []
        for i in range(0, len(nums)):
            count = 0
            for j in range(0, len(nums)):
                if nums[i] > nums[j]:
                    count = count + 1
                else:
                    pass
            result.append(count)
        return result


# testing
x = Solution()
print(x.smallerNumbersThanCurrent([6,5,4,8]))
