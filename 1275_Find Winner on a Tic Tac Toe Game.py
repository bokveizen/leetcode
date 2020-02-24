# https://leetcode-cn.com/problems/find-winner-on-a-tic-tac-toe-game/
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        state = [[None for _ in range(3)] for _ in range(3)]

        def check_win():
            if state[0] == ['A'] * 3 or state[1] == ['A'] * 3 or state[2] == ['A'] * 3 \
                    or [state[i][0] for i in range(3)] == ['A'] * 3 or [state[i][1] for i in range(3)] == ['A'] * 3 \
                    or [state[i][2] for i in range(3)] == ['A'] * 3 or [state[i][i] for i in range(3)] == ['A'] * 3 \
                    or [state[i][2 - i] for i in range(3)] == ['A'] * 3:
                return 'A'
            elif state[0] == ['B'] * 3 or state[1] == ['B'] * 3 or state[2] == ['B'] * 3 \
                    or [state[i][0] for i in range(3)] == ['B'] * 3 or [state[i][1] for i in range(3)] == ['B'] * 3 \
                    or [state[i][2] for i in range(3)] == ['B'] * 3 or [state[i][i] for i in range(3)] == ['B'] * 3 \
                    or [state[i][2 - i] for i in range(3)] == ['B'] * 3:
                return 'B'
            elif all(state[0]) and all(state[1]) and all(state[2]):
                return 'Draw'
            else:
                return 'Pending'

        current_player = 'A'
        for move in moves:
            state[move[0]][move[1]] = current_player
            if current_player == 'A':
                current_player = 'B'
            else:
                current_player = 'A'
        return check_win()
