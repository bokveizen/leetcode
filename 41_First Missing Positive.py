# https://leetcode-cn.com/problems/first-missing-positive/
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 1
        for i in range(n):
            while nums[i] != i + 1 and 1 <= nums[i] <= n:  # positive num not in the place
                tgt_pos = nums[i] - 1
                nums[i], nums[tgt_pos] = nums[tgt_pos], nums[i]
                if nums[i] == nums[tgt_pos]:
                    break
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
