# https://leetcode-cn.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        res = min(height[left], height[right]) * (right - left)
        while left < right:
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
            new_res = min(height[left], height[right]) * (right - left)
            res = max(res, new_res)
        return res
