# https://leetcode-cn.com/problems/length-of-last-word/
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        res = 0
        pos = len(s) - 1
        flag = False
        while True:
            if pos < 0 or (s[pos] == ' ' and flag):
                return res
            elif s[pos] == ' ':
                pos -= 1
            else:
                flag = True
                res += 1
                pos -= 1

