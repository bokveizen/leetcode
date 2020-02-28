# https://leetcode-cn.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = 0
        y = x
        if x == 0 or x % 10 == x:
            return True
        else:
            if x != abs(x) or x % 10 == 0:
                return False
            else:
                while y != 0:
                    res = res * 10 + y % 10
                    y //= 10
                if res == x:
                    return True
                else:
                    return False
