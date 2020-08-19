# https://leetcode-cn.com/problems/palindromic-substrings/
class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        t = '#'.join('^' + s + '$')
        n = len(t)
        p = [0] * n
        c = r = 0  # c for centre, r for right
        for i in range(1, n - 1):
            p[i] = min(r - i, p[2 * c - i]) if r > i else 1
            while t[i + p[i]] == t[i - p[i]]:
                p[i] += 1
            if i + p[i] > r:
                c, r = i, i + p[i]
        return sum(x >> 1 for x in p[1:-1])
