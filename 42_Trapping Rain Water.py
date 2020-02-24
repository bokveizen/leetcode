# https://leetcode-cn.com/problems/trapping-rain-water/
class Solution:
    def trap(self, height: List[int]) -> int:
        # remove useless bars
        while len(height) >= 2 and height[1] >= height[0]:
            height = height[1:]
        while len(height) >= 2 and height[-2] >= height[-1]:
            height = height[:-1]
        if len(height) <= 2:
            return 0
        res = 0
        # left to right
        left = 0
        tmp = 0
        for i in range(1, len(height)):
            if height[i] < height[left]:
                tmp += height[left] - height[i]
            else:
                res += tmp
                left = i
                tmp = 0
        # right to left
        right = len(height) - 1
        tmp = 0
        for i in range(len(height) - 2, left - 1, -1):
            if height[i] < height[right]:
                tmp += height[right] - height[i]
            else:
                res += tmp
                right = i
                tmp = 0
        return res
class Solution:
    def trap(self, height: List[int]) -> int:
        # remove useless bars
        while len(height) >= 2 and height[1] >= height[0]:
            height = height[1:]
        while len(height) >= 2 and height[-2] >= height[-1]:
            height = height[:-1]
        if len(height) <= 2:
            return 0
        res = 0
        left = 0
        right = len(height) - 1
        l_max = height[left]
        r_max = height[right]
        while left <= right:
            if height[left] > l_max:
                l_max = height[left]
            if height[right] > r_max:
                r_max = height[right]
            if l_max < r_max:
                res += l_max - height[left]
                left += 1
            else:
                res += r_max - height[right]
                right -= 1
        return res