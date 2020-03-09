# https://leetcode-cn.com/problems/set-matrix-zeroes/
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        m = len(matrix)
        n = len(matrix[0])
        first_row_0 = False
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    matrix[i][0] = 0
                    if j == 0:
                        first_row_0 = True
                    else:
                        matrix[0][j] = 0
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            for j in range(1, n):
                matrix[0][j] = 0
        if first_row_0:
            for i in range(m):
                matrix[i][0] = 0
