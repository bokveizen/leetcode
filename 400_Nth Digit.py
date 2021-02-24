# https://leetcode-cn.com/problems/nth-digit/
class Solution:
    def findNthDigit(self, n: int) -> int:
        digit = 1
        while n > 9 * pow(10, digit - 1) * digit:
            n -= 9 * pow(10, digit - 1) * digit
            digit += 1
        num = pow(10, digit - 1) - 1 + n // digit + (n % digit > 0)
        return int(str(num)[n % digit - 1])
