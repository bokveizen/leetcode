# https://leetcode-cn.com/problems/get-maximum-in-generated-array/
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n <= 1:
            return n
        nums = [0] * (n + 1)
        nums[1] = 1
        m = 1
        for i in range(2, n + 1):
            if i % 2:
                nums[i] = nums[i // 2] + nums[i // 2 + 1]
            else:
                nums[i] = nums[i // 2]
            m = max(m, nums[i])
        return m
