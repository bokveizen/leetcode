# https://leetcode-cn.com/problems/palindrome-partitioning-ii/
import functools
class Solution:
    @functools.lru_cache(None)
    def minCut(self, s: str) -> int:
        if s == s[::-1]:
            return 0
        ans = len(s) - 1
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:
                ans = min(self.minCut(s[i:]) + 1, ans)
        return ans


class Solution:
    def minCut(self, s: str) -> int:
        if s == s[::-1]:
            return 0
        n = len(s)
        dp_res = list(range(n))
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1):
                if (s[i] == s[j]) and (i - j <= 2 or dp[j + 1][i - 1]):
                    dp[j][i] = True
                    if j == 0:
                        dp_res[i] = 0
                    else:
                        dp_res[i] = min(dp_res[i], dp_res[j - 1] + 1)
        return dp_res[-1]




# TIMEOUT
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        if n == 0:
            return [[]]
        if n == 1:
            return [[s]]
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1):
                if (s[i] == s[j]) and (i - j <= 2 or dp[j + 1][i - 1]):
                    dp[j][i] = True
        res = []

        def backtrack(start=0, res_tmp=None):
            if res_tmp is None:
                res_tmp = []
            if start == n:
                res.append(res_tmp)
                return
            for end in range(start, n):
                if dp[start][end]:
                    backtrack(end + 1, res_tmp + [s[start:end + 1]])

        backtrack()
        return res

    def minCut(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return 0
        return min(len(a) - 1 for a in self.partition(s))


class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return 0
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1):
                if (s[i] == s[j]) and (i - j <= 2 or dp[j + 1][i - 1]):
                    dp[j][i] = True
        res = n - 1

        def backtrack(start=0, res_tmp=-1):
            if start == n:
                nonlocal res
                res = min(res, res_tmp)
                return
            for end in range(start, n):
                if dp[start][end]:
                    backtrack(end + 1, res_tmp + 1)

        backtrack()
        return res
