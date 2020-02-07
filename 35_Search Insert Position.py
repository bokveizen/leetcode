# https://leetcode-cn.com/problems/search-insert-position/
class SolutionLinearSearch:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        if target <= nums[0]:
            return 0
        if target == nums[-1]:
            return len(nums) - 1
        if target > nums[-1]:
            return len(nums)
        # nums[0] < target < nums[-1]
        res = 0
        while res < len(nums) - 1:
            if target <= nums[res + 1]:
                return res + 1
            res += 1


class SolutionBisection:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        if target <= nums[0]:
            return 0
        if target == nums[-1]:
            return len(nums) - 1
        if target > nums[-1]:
            return len(nums)
        left = 0
        right = len(nums) - 1
        # nums[left] < target < nums[right]
        while right >= left + 2:
            mid = (left + right) // 2
            if nums[mid - 1] < target <= nums[mid]:
                return mid
            elif target == nums[mid - 1]:
                return mid - 1
            elif target < nums[mid - 1]:
                right = mid - 1
            else:  # target > nums[mid]
                left = mid
        return right

