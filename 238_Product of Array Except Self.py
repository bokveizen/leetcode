# https://leetcode-cn.com/problems/product-of-array-except-self/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]
        # Now, res = Left product
        R = 1
        for i in reversed(range(len(nums))):
            res[i] *= R
            R *= nums[i]
        return res
