class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    if i == 0:
                        res += 1
                    elif grid[i - 1][j] == 0:
                        res += 1
                    if j == 0:
                        res += 1
                    elif grid[i][j - 1] == 0:
                        res += 1
        return res * 2
