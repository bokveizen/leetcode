# https://leetcode-cn.com/problems/monotonic-array/
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        l = len(A)
        if l == 1:
            return True
        i = 0
        while i + 1 < l and A[i + 1] == A[i]:
            i += 1
        if i == l - 1 or i == l - 2:
            return True
        current_dif = A[i + 1] - A[i]
        while i + 2 < l:
            next_dif = A[i + 2] - A[i + 1]
            if current_dif * next_dif < 0:
                return False
            i += 1
        return True
