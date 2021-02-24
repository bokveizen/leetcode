# https://leetcode-cn.com/problems/number-of-good-pairs/
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = [0] * 100
        res = 0
        for num in nums:
            res += counts[num - 1]
            counts[num - 1] += 1
        return res
