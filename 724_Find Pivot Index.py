# https://leetcode-cn.com/problems/find-pivot-index/
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = len(nums)
        total_sum = sum(nums)
        current_sum = 0
        for i in range(l):
            if current_sum * 2 + nums[i] == total_sum:
                return i
            else:
                current_sum += nums[i]
                i += 1
        return -1
