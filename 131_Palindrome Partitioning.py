# https://leetcode-cn.com/problems/palindrome-partitioning/
# backtrack
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        if n == 0:
            return [[]]
        if n == 1:
            return [[s]]
        res = []

        def backtrack(cur_s, res_tmp=None):
            if res_tmp is None:
                res_tmp = []
            if not cur_s:
                res.append(res_tmp)
                return
            for i in range(1, len(cur_s) + 1):
                if cur_s[:i] == cur_s[:i][::-1]:
                    backtrack(cur_s[i:], res_tmp + [cur_s[:i]])

        backtrack(s)
        return res


# DP + backtrack
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
