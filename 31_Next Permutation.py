# https://leetcode-cn.com/problems/next-permutation/
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            pass
        found = False
        for i in range(len(nums) - 1):
            if nums[-i - 1] > nums[-i - 2]:
                found = True
                for j in range(-1, -i - 2, -1):
                    if nums[j] > nums[-i - 2]:
                        nums[j], nums[-i - 2] = nums[-i - 2], nums[j]
                        nums[-i - 1:] = nums[-i - 1:][::-1]
                        break
                break
        if not found:
            nums[:] = nums[::-1]

