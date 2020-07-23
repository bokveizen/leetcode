# https://leetcode-cn.com/problems/nth-magical-number/
class Solution:
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        # def gcd(a, b):
        #     a, b = (a, b) if a >= b else (b, a)
        #     while b:
        #         a, b = b, a % b
        #     return a
        # def lcm(a, b):
        #     return a * b // gcd(a, b)
        # g = gcd(A, B)
        # l = A * B // g
        if A == B:
            return A * N
        ptr_a = A
        ptr_b = B
        basic = []
        while not basic or basic[-1] % A or basic[-1] % B:
            if ptr_a < ptr_b:
                basic.append(ptr_a)
                ptr_a += A
            else:
                basic.append(ptr_b)
                ptr_b += B
            if len(basic) == N:
                return basic[-1]
        group_i = (N - 1) // len(basic)
        return basic[(N - 1) % len(basic)] + basic[-1] * group_i

