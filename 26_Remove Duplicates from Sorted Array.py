# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        current_val = nums[0]
        count = 1
        for num in nums[1:]:
            if num != current_val:
                count += 1
                current_val = num
        return count
