# https://leetcode-cn.com/problems/number-of-music-playlists/
from functools import lru_cache


# DP
class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i == 0:
                return 1 if j == 0 else 0
            res = dp(i - 1, j - 1) * (N - j + 1) + dp(i - 1, j) * max(j - K, 0)
            return res % (10 ** 9 + 7)

        return dp(L, N)


# DP + MATH
class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        dp = [1] * (L - N + 1)
        for p in range(2, N - K + 1):
            for i in range(1, L - N + 1):
                dp[i] += dp[i - 1] * p
        res = dp[-1]
        for k in range(2, N + 1):
            res *= k
        return res % (10 ** 9 + 7)


# class Solution:
#     def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
#         res = 0
#
#         def backtrack(last_pos=None, not_used=None, cur_pos=0, flag=False):
#             if last_pos is None:
#                 last_pos = [-1] * N
#             if not_used is None:
#                 not_used = set(list(range(N)))
#             if cur_pos == L:
#                 nonlocal res
#                 res += 1
#                 return
#             remaining = L - cur_pos
#             if not flag and remaining == len(not_used):
#                 flag = True
#             if flag:  # candidates can only be in not_use
#                 for i in not_used:
#                     if last_pos[i] == -1 or cur_pos - last_pos[i] > K:
#                         new_not_used = not_used.copy()
#                         new_not_used.remove(i)
#                         new_last_pos = last_pos.copy()
#                         new_last_pos[i] = cur_pos
#                         backtrack(new_last_pos, new_not_used, cur_pos + 1, flag)
#             else:
#                 for i in range(N):
#                     if last_pos[i] == -1 or cur_pos - last_pos[i] > K:
#                         if i in not_used:
#                             new_not_used = not_used.copy()
#                             new_not_used.remove(i)
#                         else:
#                             new_not_used = not_used.copy()
#                         new_last_pos = last_pos.copy()
#                         new_last_pos[i] = cur_pos
#                         backtrack(new_last_pos, new_not_used, cur_pos + 1, flag)
#
#         backtrack()
#         return res
