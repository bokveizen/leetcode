# https://leetcode-cn.com/problems/find-the-difference/
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s = dict()
        for ch in s:
            if ch not in count_s:
                count_s[ch] = 1
            else:
                count_s[ch] += 1
        for ch in t:
            if ch not in count_s or count_s[ch] == 0:
                return ch
            else:
                count_s[ch] -= 1

# ASCII
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s = 0
        for ch in s:
            count_s -= ord(ch)
        for ch in t:
            count_s += ord(ch)
        return chr(count_s)

# bit operation
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s = 0
        for ch in s:
            count_s ^= ord(ch)
        for ch in t:
            count_s ^= ord(ch)
        return chr(count_s)
