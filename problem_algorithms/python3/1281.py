class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nums = [int(s) for s in str(n)]
        product = 1
        for m in nums:
            product *= m
        return product-sum(nums)

