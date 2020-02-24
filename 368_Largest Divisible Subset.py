# https://leetcode-cn.com/problems/largest-divisible-subset/
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        raw_list = nums
        nums.sort()
        dp = [[num] for num in nums]
        for i in range(1, len(dp)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[j]) + 1 > len(dp[i]):  # a better pre-choice
                    dp[i] = dp[j] + [nums[i]]
        longest_list = []
        for i in dp:
            if len(i) > len(longest_list):
                longest_list = i
        res = []
        for i in raw_list:
            if i in longest_list:
                res.append(i)
        return res
