# https://leetcode-cn.com/problems/jump-game-ii/
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0 for _ in nums]
        n = len(nums)
        if n <= 1:
            return 0
        for i in range(n - 1):
            pos = -2 - i
            jump_range = nums[pos]
            if jump_range >= i + 1:
                dp[pos] = 1
            elif jump_range == 0:
                dp[pos] = n
            else:
                dp[pos] = min(dp[pos + 1:pos + jump_range + 1]) + 1
        return dp[0]


class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0 for _ in nums]
        n = len(nums)
        if n <= 1:
            return 0
        for i in range(n):
            nums[i] += i
        res = 0
        current_pos = 0
        while True:
            next_pos_max = nums[current_pos]
            if next_pos_max >= n - 1:
                return res + 1
            tmp = current_pos
            for i in range(current_pos + 1, next_pos_max + 1):
                if nums[i] >= tmp:
                    current_pos = i
                    tmp = nums[i]
            res += 1
            if current_pos >= n - 1:
                return res
            if tmp >= n - 1:
                return res + 1

