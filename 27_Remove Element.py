# https://leetcode-cn.com/problems/remove-element/
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if val not in nums:
            return len(nums)
        count = 0
        for num in nums:
            if num != val:
                nums[count] = num
                count += 1
        return count
