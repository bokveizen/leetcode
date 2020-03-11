# https://leetcode-cn.com/problems/maximal-rectangle/
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:  # Q84
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

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if j == 0:
                    dp[0][i] = 1 if matrix[i][j] == '1' else 0
                else:
                    dp[j][i] = dp[j - 1][i] + 1 if matrix[i][j] == '1' else 0
        return max(self.largestRectangleArea(heights) for heights in dp)
