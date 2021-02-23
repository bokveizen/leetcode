# https://leetcode-cn.com/problems/word-break-ii/
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s:
            return False
        n = len(s)
        dp = [[] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(i):
                if j == 0 and s[:i] in wordDict:
                    dp[i].append(s[:i])
                elif dp[j] and s[j:i] in wordDict:
                    dp[i] += [p + ' ' + s[j:i] for p in dp[j]]
        return dp[-1]


# backtrack with cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        @lru_cache(None)
        def backtrack(index: int) -> List[List[str]]:
            if index == len(s):
                return [[]]
            ans = list()
            for i in range(index + 1, len(s) + 1):
                word = s[index:i]
                if word in wordSet:
                    nextWordBreaks = backtrack(i)
                    for nextWordBreak in nextWordBreaks:
                        ans.append(nextWordBreak.copy() + [word])
            return ans

        wordSet = set(wordDict)
        breakList = backtrack(0)
        return [" ".join(words[::-1]) for words in breakList]
