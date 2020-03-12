# https://leetcode-cn.com/problems/distinct-subsequences/
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0
        if len(s) == len(t):
            return int(s == t)
        # len(s) > len(t)
        len_s = len(s)
        len_t = len(t)
        dp = [[0 for _ in range(len_t + 1)] for _ in range(len_s + 1)]
        # for (s[i], t[j]), we can use t[j] or not use t[j]
        for i in range(len_s + 1):
            dp[i][0] = 1  # in consistence with ('', '') --> 1
        for i in range(1, len_s + 1):
            for j in range(1, len_t + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]
