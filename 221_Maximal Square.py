# https://leetcode-cn.com/problems/maximal-square/
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        if len(matrix) == 1:
            return int(any(data == '1' for data in matrix[0]))
        if len(matrix[0]) == 1:
            return int(any(row[0] == '1' for row in matrix))
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                elif matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                if dp[i][j] > res:
                    res = dp[i][j]
        return res * res
