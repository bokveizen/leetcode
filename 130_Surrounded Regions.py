# https://leetcode-cn.com/problems/surrounded-regions/
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m = len(board)
        n = len(board[0])
        queue = []
        for i in range(n):
            if board[0][i] == 'O':
                queue.append((0, i))
                board[0][i] = 'S'
        if m != 1:
            for i in range(n):
                if board[m - 1][i] == 'O':
                    queue.append((m - 1, i))
                    board[m - 1][i] = 'S'
        if n > 2:
            for i in range(1, m):
                if board[i][0] == 'O':
                    queue.append((i, 0))
                    board[i][0] = 'S'
                if board[i][n - 1] == 'O':
                    queue.append((i, n - 1))
                    board[i][n - 1] = 'S'
        while queue:
            current_pos = queue.pop(0)
            for direction in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                next_pos = (current_pos[0] + direction[0],
                            current_pos[1] + direction[1])
                if 0 <= next_pos[0] < m and 0 <= next_pos[1] < n \
                        and board[next_pos[0]][next_pos[1]] == 'O':
                    queue.append(next_pos)
                    board[next_pos[0]][next_pos[1]] = 'S'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'

# 并查集
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        f = {}

        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(y)] = find(x)

        if not board or not board[0]:
            return
        row = len(board)
        col = len(board[0])
        dummy = row * col
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                        union(i * col + j, dummy)
                    else:
                        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            if board[i + x][j + y] == "O":
                                union(i * col + j, (i + x) * col + (j + y))
        for i in range(row):
            for j in range(col):
                if find(dummy) == find(i * col + j):
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
