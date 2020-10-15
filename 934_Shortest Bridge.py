# https://leetcode-cn.com/problems/shortest-bridge/
class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        island0 = []
        island1 = []
        n = len(A)
        # put the first 1 in island0
        for i in range(n):
            for j in range(n):
                if A[i][j]:
                    island0.append((i, j))
                    A[i][j] = -1
                    break
            else:
                continue
            break
        cur = island0[:]
        while cur:
            x, y = cur.pop()
            # to_check = [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]
            to_check = []
            if x > 0:
                to_check.append((x - 1, y))
            if x + 1 < n:
                to_check.append((x + 1, y))
            if y > 0:
                to_check.append((x, y - 1))
            if y + 1 < n:
                to_check.append((x, y + 1))
            for x, y in to_check:
                if A[x][y] == 1:
                    cur.append((x, y))
                    island0.append((x, y))
                    A[x][y] = -1

        # # the remaining 1s constitute island1
        # for i in range(n):
        #     for j in range(n):
        #         if A[i][j] and (i, j) not in island0:
        #             island1.append((i, j))
        # # res = min(Manhattan distance(a, b)) - 1 for a in island0 for b in island 1
        # res = 2 * n
        # for x0, y0 in island0:
        #     for x1, y1 in island1:
        #         res = min(res, abs(x0 - x1) + abs(y0 - y1))
        #         if res == 2:
        #             return 1
        # return res - 1

        while True:
            x, y = island0.pop(0)
            v = A[x][y]
            to_check = []
            if x > 0:
                to_check.append((x - 1, y))
            if x + 1 < n:
                to_check.append((x + 1, y))
            if y > 0:
                to_check.append((x, y - 1))
            if y + 1 < n:
                to_check.append((x, y + 1))
            for xt, yt in to_check:
                if A[xt][yt] == 1:  # island1
                    return - v - 1
                elif A[xt][yt] == 0:  # empty land
                    A[xt][yt] = v - 1
                    island0.append((xt, yt))

