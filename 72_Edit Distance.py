# https://leetcode-cn.com/problems/edit-distance/
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        dp = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        for i in range(len(word2)+1):
            dp[0][i] = i
        for i in range(len(word1)+1):
            dp[i][0] = i
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                dp[i][j] = min(
                    dp[i - 1][j] + 1,
                    dp[i][j - 1] + 1,
                    dp[i - 1][j - 1] + (word1[i-1] != word2[j-1])
                )
        return dp[-1][-1]
