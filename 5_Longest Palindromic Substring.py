# https://leetcode-cn.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        dp = [[0 for _ in s] for _ in s]
        res = [0, 0]
        for i in range(len(s)):
            dp[i][i] = 1
        for j in range(1, len(s)):
            for i in range(j):
                if s[i] == s[j]:
                    if j - i <= 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False
                if dp[i][j] and j - i > res[1] - res[0]:
                    res = [i, j]
        return s[res[0]:res[1] + 1]
