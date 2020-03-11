# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        j = 1
        cnt = 1
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                cnt += 1
            else:
                cnt = 1
            if cnt <= 2:
                if i != j:
                    nums[j] = nums[i]
                j += 1
        return j
