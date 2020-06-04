# https://leetcode-cn.com/problems/house-robber/
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        a, b, c = nums[0], nums[1], nums[0] + nums[2]
        for i in range(3, n):
            a, b, c = b, c, max(a, b) + nums[i]
        return max(b, c)
