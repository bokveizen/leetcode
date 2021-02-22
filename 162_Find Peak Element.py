# https://leetcode-cn.com/problems/find-peak-element/

# linear
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[n - 1] > nums[n - 2]:
            return n - 1
        left = 0
        right = n - 1
        while right > left:
            if right == left + 2:
                return left + 1
            if nums[left + 1] > nums[left + 2]:
                return left + 1
            else:
                left += 1
            if nums[right - 1] > nums[right - 2]:
                return right - 1
            else:
                right -= 1


# logarithmic (binary search)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[n - 1] > nums[n - 2]:
            return n - 1
        left = 0
        right = n - 1
        while right > left:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left
