# https://leetcode-cn.com/problems/search-in-rotated-sorted-array/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while right >= left + 2:
            mid = (left + right) // 2
            if nums[mid] > nums[left]:  # left - mid is in order
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:  # mid - right is in order
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid - 1
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1
