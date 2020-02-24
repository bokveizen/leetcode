# https://leetcode-cn.com/problems/happy-number/
class Solution:
    def isHappy(self, n: int) -> bool:
        res_list = [n]
        num = n
        while True:
            res = 0
            while num >= 1:
                last_digit = num % 10
                res += last_digit * last_digit
                num //= 10
            if res == 1:
                return True
            if res in res_list:
                return False
            res_list.append(res)
            num = res

