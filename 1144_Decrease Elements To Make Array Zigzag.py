# https://leetcode-cn.com/problems/decrease-elements-to-make-array-zigzag/
class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        if n == 2:
            return 1 if nums[0] == nums[1] else 0
        res1 = res2 = 0
        tmp = nums[:]
        for i in range(1, n, 2):
            if i == n - 1:
                if nums[i - 1] >= nums[i]:
                    res1 += nums[i - 1] - (nums[i] - 1)
            else:
                if not nums[i - 1] < nums[i] > nums[i + 1]:
                    if nums[i - 1] >= nums[i]:
                        res1 += nums[i - 1] - (nums[i] - 1)
                    if nums[i + 1] >= nums[i]:
                        res1 += nums[i + 1] - (nums[i] - 1)
                        nums[i + 1] = nums[i] - 1
        nums = tmp[:]
        for i in range(0, n, 2):
            if i == 0:
                if nums[i + 1] >= nums[i]:
                    res2 += nums[i + 1] - (nums[i] - 1)
                    nums[i + 1] = nums[i] - 1
            elif i == n - 1:
                if nums[i - 1] >= nums[i]:
                    res2 += nums[i - 1] - (nums[i] - 1)
            else:
                if not nums[i - 1] < nums[i] > nums[i + 1]:
                    if nums[i - 1] >= nums[i]:
                        res2 += nums[i - 1] - (nums[i] - 1)
                    if nums[i + 1] >= nums[i]:
                        res2 += nums[i + 1] - (nums[i] - 1)
                        nums[i + 1] = nums[i] - 1
        return min(res1, res2)
