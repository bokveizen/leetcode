# https://leetcode-cn.com/problems/minimum-path-sum/
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = grid
        m = len(dp)
        n = len(dp[0])
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue
                if i == 0:
                    dp[i][j] += dp[i][j-1]
                elif j == 0:
                    dp[i][j] += dp[i-1][j]
                else:
                    dp[i][j] += min(dp[i][j-1], dp[i-1][j])
        return dp[-1][-1]
