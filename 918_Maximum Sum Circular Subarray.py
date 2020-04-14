# https://leetcode-cn.com/problems/maximum-sum-circular-subarray/
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        n = len(A)
        if n == 1:
            return A[0]
        if n == 2:
            return max(max(A), sum(A))
        if n == 3:
            return max(max(A), sum(A) - min(A), sum(A))
        kadane_res = temp = A[0]
        for i in range(1, n):
            temp = A[i] if temp <= 0 else A[i] + temp
            kadane_res = max(kadane_res, temp)
        kadane_inverse_res = temp = A[1]
        for i in range(2, n - 1):
            temp = A[i] if temp >= 0 else A[i] + temp
            kadane_inverse_res = min(kadane_inverse_res, temp)
        return max(kadane_res, sum(A) - kadane_inverse_res)
