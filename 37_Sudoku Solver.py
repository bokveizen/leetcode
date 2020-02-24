# https://leetcode-cn.com/problems/sudoku-solver/
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [[0 for _ in range(10)] for _ in range(9)]
        col = [[0 for _ in range(10)] for _ in range(9)]
        sub = [[0 for _ in range(10)] for _ in range(9)]
        solved = False

        def backtrack(i=0, j=0):
            nonlocal solved
            if board[i][j] == '.':
                for num in range(1, 10):
                    if place_available_check(num, i, j):
                        place(num, i, j)
                        if i == j == 8:
                            solved = True
                        else:
                            if j == 8:
                                backtrack(i + 1, 0)
                            else:
                                backtrack(i, j + 1)
                        if not solved:
                            remove(num, i, j)
            else:
                if i == j == 8:
                    solved = True
                else:
                    if j == 8:
                        backtrack(i + 1, 0)
                    else:
                        backtrack(i, j + 1)

        def place_available_check(num, i, j):
            row_i = i
            col_i = j
            sub_i = (i // 3) * 3 + j // 3
            return not (row[row_i][num] or col[col_i][num] or sub[sub_i][num])

        def place(num, i, j):
            row_i = i
            col_i = j
            sub_i = (i // 3) * 3 + j // 3
            row[row_i][num] = col[col_i][num] = sub[sub_i][num] = 1
            board[row_i][col_i] = str(num)

        def remove(num, i, j):
            row_i = i
            col_i = j
            sub_i = (i // 3) * 3 + j // 3
            row[row_i][num] = col[col_i][num] = sub[sub_i][num] = 0
            board[row_i][col_i] = '.'

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    place(num, i, j)
        backtrack()
