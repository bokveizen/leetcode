# https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        left = 0
        right = len(nums) - 1
        while right >= left + 2:
            mid = (left + right) // 2
            if nums[mid] > nums[left]:  # left - mid is in order
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            elif nums[mid] < nums[right]:  # mid - right is in order
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid - 1
            else:
                if nums[mid] == nums[left]:
                    left += 1
                if nums[mid] == nums[right]:
                    right -= 1
        if nums[left] == target or nums[right] == target:
            return True
        return False
