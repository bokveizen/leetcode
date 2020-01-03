# https://leetcode-cn.com/problems/reshape-the-matrix/
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        r0 = len(nums)
        c0 = len(nums[0])
        if r0 * c0 != r * c:
            return nums
        nums_one_line = sum(nums, [])
        return [nums_one_line[i * c:(i + 1) * c] for i in range(r)]
