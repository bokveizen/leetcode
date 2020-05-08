# https://leetcode-cn.com/problems/maximum-width-ramp/
class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        n = len(A)
        if n < 2:
            return 0
        res = 0
        MAX = 50000
        min_i = MAX + 1
        for i in sorted(range(n), key=lambda x: A[x]):
            res = max(res, i - min_i)
            min_i = min(min_i, i)
        return res
