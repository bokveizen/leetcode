# https://leetcode-cn.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        res = [0] * n
        res[0] = 1
        res[1] = 2
        pos = 2
        while pos < n:
            res[pos] = res[pos - 1] + res[pos - 2]
            pos += 1
        return res[-1]
