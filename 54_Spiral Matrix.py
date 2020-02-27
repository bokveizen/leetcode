# https://leetcode-cn.com/problems/spiral-matrix/
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        if m == 0:
            return []
        if m == 1:
            return matrix[0]
        n = len(matrix[0])
        if n == 1:
            return [row[0] for row in matrix]
        r = 0
        mm = m
        nn = n
        res = []
        while mm and nn:
            if mm >= 2 and nn >= 2:
                # line 1
                res += matrix[r][r:-1 - r]
                # line 2
                res += [matrix[i][-1 - r] for i in range(r, m - 1 - r)]
                # line 3
                res += matrix[m - 1 - r][-1 - r:r:-1]
                # line 4
                res += [matrix[i][r] for i in range(m - 1 - r, r, -1)]
                # parameters change
                r += 1
                mm -= 2
                nn -= 2
            elif mm == 1:  # last row
                res += matrix[r][r:n - r]
                mm = 0
            else:  # nn == 1
                res += [matrix[i][r] for i in range(r, m - r)]
                nn = 0
        return res
