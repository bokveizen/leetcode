# https://leetcode-cn.com/problems/random-pick-index/
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.len = len(nums)

    def pick(self, target: int) -> int:
        res = -1
        cnt = 0
        for i in range(self.len):
            if self.nums[i] == target:
                if res == -1 or random.randint(1, cnt + 1) == 1:
                    res = i
                cnt += 1
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)