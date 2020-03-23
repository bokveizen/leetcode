# https://leetcode-cn.com/problems/longest-palindrome/
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return 1
        cnt = Counter(s)
        res = 0
        odd_exist = False
        for char in cnt:
            if not odd_exist and cnt[char] % 2:
                odd_exist = True
            res += cnt[char] - cnt[char] % 2
        return res + 1 if odd_exist else res
