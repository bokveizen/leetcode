# https://leetcode-cn.com/problems/base-7/
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        minus = num < 0
        if minus:
            num = -num
        res = ''
        while num:
            res = str(num % 7) + res
            num //= 7
        return '-' + res if minus else res
