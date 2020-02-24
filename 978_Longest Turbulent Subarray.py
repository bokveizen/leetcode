# https://leetcode-cn.com/problems/longest-turbulent-subarray/
class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        if len(A) == 1:
            return 1
        A_dif = [A[i + 1] - A[i] for i in range(len(A) - 1)]
        i = 0
        while i < len(A_dif):
            if A_dif[i] == 0:
                i += 1
            else:
                break
        if i == len(A_dif) - 1:
            return 2
        if i == len(A_dif):
            return 1
        current_dif = A_dif[i]
        tmp = 2
        res = 2
        for i in range(i + 1, len(A_dif)):
            if current_dif * A_dif[i] < 0:
                current_dif = A_dif[i]
                tmp += 1
            elif A_dif[i] == 0:
                res = max(res, tmp)
                tmp = 1
                current_dif = 0
            else:
                res = max(res, tmp)
                tmp = 2
                current_dif = A_dif[i]
        res = max(res, tmp)
        return res
