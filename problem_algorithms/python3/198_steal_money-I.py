from typing import List


class Solution1:
    def maxSum(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        temp = []
        for i in range(len(nums)):
            if nums[i] >= 0:
                temp.append(nums[i])
            else:
                temp.append(0)
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for j in range(2, len(nums)):
            dp[j] = max(nums[j]+dp[j-2], dp[j-1])
        return dp[len(nums)-1]
