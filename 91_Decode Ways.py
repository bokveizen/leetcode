# https://leetcode-cn.com/problems/decode-ways/
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        if s[0] == '0':
            return 0
        n = len(s)
        if n == 1:
            return 1
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            if s[i - 1] == '0':
                if s[i - 2] in '12':
                    dp[i] = dp[i - 2]
                else:
                    return 0
            elif s[i - 2] == '1' or (s[i - 2] == '2' and s[i - 1] in '123456'):
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]
        return dp[-1]
