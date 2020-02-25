# https://leetcode-cn.com/problems/wildcard-matching/
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        len_s = len(s)
        len_p = len(p)
        # dp[i][j] = the matchability of p[:i] and s[:j]
        dp = [[False for _ in range(len_s + 1)] for _ in range(len_p + 1)]
        dp[0][0] = True
        for i in range(1, len_p + 1):
            if p[i - 1] == '*':
                dp[i][0] = dp[i - 1][0]
            else:
                break
        for i in range(1, len_p + 1):
            for j in range(1, len_s + 1):
                if p[i - 1] == s[j - 1] or p[i - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[i - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        return dp[-1][-1]
