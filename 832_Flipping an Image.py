# https://leetcode-cn.com/problems/flipping-an-image/
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        n = len(A)
        res = []
        for i in range(n):
            row = []
            for j in range(1, n + 1):
                row.append(1 - A[i][-j])
            res.append(row)
        return res
