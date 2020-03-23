# https://leetcode-cn.com/problems/word-break/
# backtrack (can pass w/ lru_cache or memo)
from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return False
        n = len(s)

        @lru_cache(None)
        def backtrack(start=0):
            if start == n:
                return True
            for i in range(start + 1, n + 1):
                if s[start:i] in wordDict and backtrack(i):
                    return True
            return False

        return backtrack()


# BFS/DFS
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return False
        n = len(s)
        visited = set()
        queue = [0]
        while queue:
            start = queue.pop()  # queue.pop(0) for BFS
            if start not in visited:
                for i in range(start + 1, n + 1):
                    if s[start:i] in wordDict:
                        if i == n:
                            return True
                        queue.append(i)
                visited.add(start)
        return False


# DP
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return False
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = 1
                    break
        return bool(dp[-1])








