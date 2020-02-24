# https://leetcode-cn.com/problems/triangle/
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        temp = triangle[-1]  # triangle[n-1]
        while True:
            if n == 1:
                return temp[0]
            temp = [min(temp[i], temp[i + 1]) for i in range(n - 1)]
            n -= 1
            for i in range(n):
                temp[i] += triangle[n - 1][i]
