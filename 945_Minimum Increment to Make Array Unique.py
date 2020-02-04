# https://leetcode-cn.com/problems/minimum-increment-to-make-array-unique/
# ref: https://leetcode-cn.com/problems/minimum-increment-to-make-array-unique/solution/pa-jie-ti-ono1python3-by-cowry/
class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if not A:
            return 0
        A.sort()
        res = step = 0
        for i in range(len(A)):
            if A[i] < step:
                res += step - A[i]
                step += 1
            else:
                step = A[i] + 1
        return res
