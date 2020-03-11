# https://leetcode-cn.com/problems/largest-rectangle-in-histogram/
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        if n == 0:
            return 0
        if n == 1:
            return heights[0]
        left_boarder = [-1] + [0] * (n - 1)
        right_boarder = [0] * (n - 1) + [n]
        for i in range(1, n):
            tmp = i - 1
            while tmp >= 0 and heights[tmp] >= heights[i]:
                tmp = left_boarder[tmp]
            left_boarder[i] = tmp
        for i in range(n - 2, -1, -1):
            tmp = i + 1
            while tmp < n and heights[tmp] >= heights[i]:
                tmp = right_boarder[tmp]
            right_boarder[i] = tmp
        res = 0
        for i in range(n):
            res_i = heights[i] * (right_boarder[i] - left_boarder[i] - 1)
            if res_i > res:
                res = res_i
        return res


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        if n == 0:
            return 0
        if n == 1:
            return heights[0]
        stack = [-1]
        res = 0
        for i in range(n):
            while len(stack) > 1 and heights[stack[-1]] >= heights[i]:  # keep strict monotone, non-strict is also OK
                new_res = heights[stack.pop()] * (i - stack[-1] - 1)
                if new_res > res:
                    res = new_res
            stack.append(i)
        while len(stack) > 1:
            new_res = heights[stack.pop()] * (len(heights) - stack[-1] - 1)
            if new_res > res:
                res = new_res
        return res
