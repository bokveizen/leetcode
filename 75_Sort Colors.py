# https://leetcode-cn.com/problems/sort-colors/
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return
        left = 0
        right = n - 1
        cur = 0
        # if i < left: nums[i] == 0
        # if i > right: nums[i] == 2
        # left <= cur <= right
        while cur <= right:
            if nums[cur] == 0:
                if left != cur:
                    nums[left], nums[cur] = nums[cur], nums[left]
                left += 1
                cur += 1
            elif nums[cur] == 2:
                nums[right], nums[cur] = nums[cur], nums[right]
                right -= 1
            else:
                cur += 1
