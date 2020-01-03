# https://leetcode-cn.com/problems/sum-of-square-numbers/
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        while i * i <= c:
            i += 1
        n = i
        i = 0
        j = n - 1
        while True:
            if i > j:
                return False
            if i * i + j * j == c:
                return True
            elif i * i + j * j < c:
                i += 1
            else:
                j -= 1
