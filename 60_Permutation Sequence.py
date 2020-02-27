# https://leetcode-cn.com/problems/permutation-sequence/
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if n == 1:
            return '1'
        factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        num = [str(i + 1) for i in range(n)]
        res = ''
        while n >= 2:
            current = (k - 1) // factorial[n - 1]
            res += num.pop(current)
            k = k % factorial[n - 1]
            n -= 1
        return res + num[0]
