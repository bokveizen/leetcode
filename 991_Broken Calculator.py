# https://leetcode-cn.com/problems/broken-calculator/
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        res = 0
        while Y > X:
            if Y % 2:
                Y += 1
            else:
                Y >>= 1
            res += 1
        return res + X - Y