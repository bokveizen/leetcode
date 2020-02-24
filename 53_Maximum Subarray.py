# https://leetcode-cn.com/problems/maximum-subarray/
class Solution:
    # dp
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [i for i in nums]
        for i in range(1, len(dp)):
            dp[i] = max(dp[i], dp[i] + dp[i - 1])
        return max(dp)

    # divide and conquer
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        res_l = self.maxSubArray(nums[:len(nums) // 2])
        res_r = self.maxSubArray(nums[len(nums) // 2:])
        res_ml = max([sum(nums[i:len(nums) // 2]) for i in range(len(nums) // 2)])
        res_mr = max([sum(nums[len(nums) // 2:i]) for i in range(len(nums) // 2, len(nums) + 1)])
        res_m = res_ml + res_mr
        return max(res_l, res_r, res_m)
