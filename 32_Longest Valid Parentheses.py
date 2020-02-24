# https://leetcode-cn.com/problems/longest-valid-parentheses/
class Solution0:
    def longestValidParentheses(self, s: str) -> int:
        if '()' not in s:
            return 0
        n = len(s)
        valid = list(range(len(s)))
        while '()' in s:
            pos = s.index('()')
            s = s[:pos] + s[pos + 2:]
            valid = valid[:pos] + valid[pos + 2:]
        if not valid:
            return n
        res = valid[0]
        valid = [-1] + valid + [n]
        for i in range(1, len(valid) - 1):
            if valid[i + 1] - valid[i] - 1 > res:
                res = valid[i + 1] - valid[i] - 1
        return res


class SolutionStack:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        res = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
        return res


class SolutionDP:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        dp = [0] * n
        res = 0
        for i in range(n):
            if i > 0 and s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2
                elif s[i - 1] == ")" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                if dp[i] > res:
                    res = dp[i]
        return res
