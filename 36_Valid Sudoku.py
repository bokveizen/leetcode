# https://leetcode-cn.com/problems/valid-sudoku/
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[0 for _ in range(10)] for _ in range(9)]
        col = [[0 for _ in range(10)] for _ in range(9)]
        sub = [[0 for _ in range(10)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                ch = board[i][j]
                num = 0 if ch == '.' else int(ch)
                row_i = i
                col_i = j
                sub_i = (i // 3) * 3 + j // 3
                if num:
                    if row[row_i][num] or col[col_i][num] or sub[sub_i][num]:
                        return False
                    else:
                        row[row_i][num] = col[col_i][num] = sub[sub_i][num] = 1
        return True
