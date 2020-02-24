# https://leetcode-cn.com/problems/3sum/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        if len(nums) < 3:
            return sol
        nums = sorted(nums)
        i = 0
        while True:
            if nums[i] > 0 or i >= len(nums) - 2:
                return sol
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    sol.append([nums[i], nums[left], nums[right]])
                if nums[left] == nums[right]:
                    break
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                    while nums[left] == nums[left - 1]:
                        left += 1
                else:
                    right -= 1
                    while nums[right] == nums[right + 1]:
                        right -= 1
            i += 1
