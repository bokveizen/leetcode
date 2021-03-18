# https://leetcode-cn.com/problems/count-substrings-that-differ-by-one-character/
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        dp = [[[0, 0] for _ in t] for _ in s]
        m = len(s)
        n = len(t)
        res = 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = [1, 0] if s[i] == t[j] else [0, 1]
                elif s[i] == t[j]:
                    dp[i][j] = [dp[i - 1][j - 1][0] + 1, dp[i - 1][j - 1][1]]
                else:
                    dp[i][j] = [0, dp[i - 1][j - 1][0] + 1]
                res += dp[i][j][1]
        return res
