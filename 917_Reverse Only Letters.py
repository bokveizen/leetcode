# https://leetcode-cn.com/problems/reverse-only-letters/
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        letters = [c for c in S if c.isalpha()]
        res = ''
        for c in S:
            res += letters.pop() if c.isalpha() else c
        return res
