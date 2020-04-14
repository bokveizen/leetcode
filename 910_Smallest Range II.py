# https://leetcode-cn.com/problems/smallest-range-ii/
class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        if len(A) == 1:
            return 0
        A.sort()
        res = A[-1] - A[0]
        if K == 0:
            return res
        for i in range(len(A) - 1):
            # max = max(A[i]+K, A[-1]-K), min = min(A[0]+K, A[i+1]-K)
            res = min(res, max(A[i] + K, A[-1] - K) - min(A[0] + K, A[i + 1] - K))
        return res
