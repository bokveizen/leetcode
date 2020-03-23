# https://leetcode-cn.com/problems/single-number-ii/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res1 = 0
        res2 = 0
        for num in nums:
            tmp1, tmp2 = res1, res2
            res1, res2 = (tmp2 & num) | (tmp1 & ~num), ~tmp1 & (res2 ^ num)
        return res2
