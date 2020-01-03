# https://leetcode-cn.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for index, val in enumerate(nums):
            if target - val in dct:
                return [dct[target - val], index]
            dct[val] = index
