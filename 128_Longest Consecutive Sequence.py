# https://leetcode-cn.com/problems/longest-consecutive-sequence/
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        res = 1
        nums_set = set(nums)

        for num in nums_set:
            if num - 1 not in nums_set:  # it's a reasonable start of a consecutive seq
                cur = num
                cur_res = 1
                while cur + 1 in nums_set:
                    cur += 1
                    cur_res += 1
                if cur_res > res:
                    res = cur_res
        return res
