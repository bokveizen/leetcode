# https://leetcode-cn.com/problems/jump-game/
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return True
        for i in range(n):
            nums[i] += i
        current_pos = 0
        while True:
            next_pos_max = nums[current_pos]
            if next_pos_max == current_pos:
                return False
            if next_pos_max >= n - 1:
                return True
            tmp = current_pos
            for i in range(current_pos + 1, next_pos_max + 1):
                if nums[i] >= tmp:
                    current_pos = i
                    tmp = nums[i]
            if current_pos >= n - 1 or tmp >= n - 1:
                return True
