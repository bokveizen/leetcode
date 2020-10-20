# https://leetcode-cn.com/problems/squares-of-a-sorted-array/
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if A[0] >= 0:
            return [a * a for a in A]
        if A[-1] <= 0:
            return [a * a for a in A][::-1]
        l = r = 0
        for i in range(len(A)):
            if A[i] > 0:
                l = i - 1
                r = i
                break
        res = []
        while l >= 0 and r < len(A):
            if A[r] < -A[l]:
                res.append(A[r] * A[r])
                r += 1
            else:
                res.append(A[l] * A[l])
                l -= 1
        while l >= 0:
            res.append(A[l] * A[l])
            l -= 1
        while r < len(A):
            res.append(A[r] * A[r])
            r += 1

        return res
