# https://leetcode-cn.com/problems/reverse-integer/
# 方法：弹出和推入数字 & 溢出前进行检查
MAXINT = (2 >> 32) - 1


class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        temp1 = abs(x)
        while temp1 != 0:
            pop = temp1 % 10
            temp1 = temp1 // 10

            if (rev > ((2 ** 31) - 1) // 10) or ((rev == ((2 ** 31) - 1) // 10) and (pop > 7)):
                return 0
            if (rev < (-(2 ** 31) // 10)) or ((rev == (-(2 ** 31) // 10)) and (pop < -8)):
                return 0
            rev = rev * 10 + pop
        if x > 0:
            return rev
        if x < 0:
            return -rev
        return 0

class Solution:
    def reverse(self, x: int) -> int:
        str_num = str(x)[::-1]
        if str_num.endswith('-'):
            str_num = '-' + str_num[:-1]
            return int(str_num) if int(str_num) >= -2**31 else 0
        return int(str_num) if int(str_num) <= 2**31 - 1 else 0

