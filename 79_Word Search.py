# https://leetcode-cn.com/problems/word-search/
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        if not board or not board[0]:
            return False
        word_len = len(word)
        m = len(board)
        n = len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        '''
        visited = [[False]*n]*m will make m lists changed together!!!!
        '''

        def search(pos, x, y):
            if pos == word_len - 1:
                return board[x][y] == word[pos]
            if board[x][y] == word[pos]:
                visited[x][y] = True
                for direction in directions:
                    next_x = x + direction[0]
                    next_y = y + direction[1]
                    if 0 <= next_x < m and 0 <= next_y < n \
                            and not visited[next_x][next_y] \
                            and search(pos + 1, next_x, next_y):
                        return True
                visited[x][y] = False
            return False

        for i in range(m):
            for j in range(n):
                if search(0, i, j):
                    return True
        return False

