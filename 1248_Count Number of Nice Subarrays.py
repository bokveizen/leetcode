# https://leetcode-cn.com/problems/count-number-of-nice-subarrays/
from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [i % 2 for i in nums]
        odd_indexes = [-1] + [index for index, value in enumerate(nums) if value == 1] + [len(nums)]
        if len(odd_indexes) < k + 2:
            return 0
        odd_space = [(odd_indexes[i + 1] - odd_indexes[i]) for i in range(len(odd_indexes) - 1)]
        res = 0
        for i in range(len(odd_space) - k):
            res += odd_space[i] * odd_space[i + k]
        return res
