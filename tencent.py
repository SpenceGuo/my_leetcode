from typing import List


# 当数组内的数均不大于0时，程序所做的操作为不选，此时最大和为0
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        result = 0
        # 标志数组，标记哪些数字已选或未选
        tags = [0 for _ in range(len(nums))]
        # 数组为空时返回0
        if len(nums) == 0:
            return 0
        # 将大于0的先全部选择出来
        for i in range(0, len(nums)):
            if nums[i] > 0:
                result += nums[i]
                tags[i] = 1
        # 判断是否有相邻的两个数字都被选择过，有则减去小的那一个
        for j in range(0, len(nums)-1):
            if tags[j] == 1 and tags[j+1] == 1:
                result -= min(nums[j], nums[j+1])
                if nums[j] < nums[j+1]:
                    tags[j] = 0
                else:
                    tags[j+1] = 0
        # 最后判断首位两个数字是否都被选择，并作类似处理
        if tags[0] == 1 and tags[-1] == 1:
            result -= min(nums[0], nums[-1])
        # 返回最后结果
        return result


x = Solution()
print(x.maxSum([3,-1,4,3,-5,8,9]))
