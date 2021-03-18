# https://leetcode-cn.com/problems/monotone-increasing-digits/
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        N = str(N)
        n = len(N)
        if n == 1:
            return int(N)
        res = ''
        for i in range(n):
            j = i
            while j < n and N[j] == N[i]:
                j += 1
            if j == n:
                res += N[i] * (n - i)
                return int(res)
            elif int(N[j]) > int(N[i]):
                res += N[i]
                continue
            else:
                res += str(int(N[i]) - 1) + '9' * (n - i - 1)
                return int(res)
