# https://leetcode-cn.com/problems/spiral-matrix-ii/
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
            return []
        if n == 1:
            return [[1]]
        if n == 2:
            return [[1, 2],
                    [4, 3]]
        matrix = [[0] for _ in range(n) for _ in range(n)]
        nn = n
        r = 0
        num = 0
        while nn:
            if nn >= 2:
                # line 1, matrix[r][r:-1 - r]
                for i in range(r, n - 1 - r):
                    num += 1
                    matrix[r][i] = num
                # line 2, [matrix[i][-1 - r] for i in range(r, m - 1 - r)]
                for i in range(r, n - 1 - r):
                    num += 1
                    matrix[i][n - 1 - r] = num
                # line 3, matrix[m - 1 - r][-1 - r:r:-1]
                for i in range(n - 1 - r, r, -1):
                    num += 1
                    matrix[n - 1 - r][i] = num
                # line 4, [matrix[i][r] for i in range(m - 1 - r, r, -1)]
                for i in range(n - 1 - r, r, -1):
                    num += 1
                    matrix[i][r] = num
                r += 1
                nn -= 2
            else:  # nn == 1
                num += 1
                matrix[r][r] = num
        return matrix
