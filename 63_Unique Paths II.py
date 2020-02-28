# https://leetcode-cn.com/problems/unique-paths-ii/
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0
        if m == 1:
            if any(obstacleGrid[0]):
                return 0
            return 1
        if n == 1:
            if any(line[0] for line in obstacleGrid):
                return 0
            return 1
        # m, n >=2
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        for i in range(1, n):
            dp[0][i] = dp[0][i - 1] if obstacleGrid[0][i] == 0 else 0
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] if obstacleGrid[i][0] == 0 else 0
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] if obstacleGrid[i][j] == 0 else 0
        return dp[-1][-1]

