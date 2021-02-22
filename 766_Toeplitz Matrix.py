# https://leetcode-cn.com/problems/toeplitz-matrix/
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        if m == 1 or n == 1:
            return True
        # totally m + n - 1 diagonals
        for d in range(1 - n, m - 1):
            cur = -1
            for i in range(max(0, d), min(m, d + n)):
                j = i - d
                if cur == -1:
                    cur = matrix[i][j]
                elif cur != matrix[i][j]:
                    return False
        return True
