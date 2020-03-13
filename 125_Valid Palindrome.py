# https://leetcode-cn.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        nums = '0123456789'

        def same_char(c1, c2):
            if c1 in nums:
                return c1 == c2
            if c2 in alphabet:
                return c1 == c2 \
                       or ord(c1) == ord(c2) + 32 \
                       or ord(c1) == ord(c2) - 32

        n = len(s)
        if n <= 1:
            return True
        if not any(c in alphabet + nums for c in s):
            return True
        left = 0
        right = n - 1
        while left < right:
            while s[left] not in alphabet + nums:
                left += 1
            while s[right] not in alphabet + nums:
                right -= 1
            if left >= right:
                return True
            if not same_char(s[left], s[right]):
                return False
            if left >= right - 2:
                return True
            if left == right - 3:
                if s[left + 1] not in alphabet + nums or s[left + 2] not in alphabet + nums:
                    return True
            left += 1
            right -= 1

class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        if n <= 1:
            return True
        if not any(c.isalnum() for c in s):
            return True
        left = 0
        right = n - 1
        while True:
            while not s[left].isalnum():
                left += 1
            while not s[right].isalnum():
                right -= 1
            if left >= right:
                return True
            if s[left].lower() != s[right].lower():
                return False
            if left >= right - 2:
                return True
            left += 1
            right -= 1
