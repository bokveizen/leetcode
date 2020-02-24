# https://leetcode-cn.com/problems/integer-replacement/
class Solution:
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        if n % 2 == 0:
            return self.integerReplacement(n // 2) + 1
        return min(self.integerReplacement((n + 1) // 2), self.integerReplacement((n - 1) // 2)) + 2


# bin
class Solution:
    def integerReplacement(self, n: int) -> int:
        res = 0
        while True:
            if n == 1:
                return res
            if n == 3:
                n = 1
                res += 2
            elif n % 2 == 0:
                n = n >> 1
                res += 1
            elif n % 4 == 1:
                n = n >> 1
                res += 2
            elif n % 4 == 3:
                n = (n + 1) >> 1
                res += 2
