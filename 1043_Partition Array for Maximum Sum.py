# https://leetcode-cn.com/problems/partition-array-for-maximum-sum/
from typing import List


class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        if K == len(A):
            return max(A) * len(A)
        if K == 1:
            return sum(A)
        dp = [0] * (len(A) + 1)  # dp[i] = the ans of the sub-problem on A[:i]
        for i in range(1, len(A) + 1):
            j = i - 1
            tmp = 0
            while i - j <= K and j >= 0:
                if A[j] > tmp:
                    tmp = A[j]
                if dp[j] + tmp * (i - j) > dp[i]:
                    dp[i] = dp[j] + tmp * (i - j)
                j -= 1
        return dp[-1]
