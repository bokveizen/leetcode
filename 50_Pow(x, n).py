# https://leetcode-cn.com/problems/powx-n/
# 递归 Recursion
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def __help(a, b):
            if b == 1:
                return a
            elif b & 1:
                return a * __help(a, b - 1)
            elif not b & 1:
                return __help(a * a, b // 2)

        if n > 0:
            return __help(x, n)
        elif n == 0:
            return 1
        else:
            return __help(1 / x, -n)


# 迭代 Iteration
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        elif not n:
            return 1

        ans = 1
        while n > 1:
            if n & 1:
                ans *= x
                n -= 1
            else:
                x = x * x
                n //= 2
        ans *= x
        return ans
