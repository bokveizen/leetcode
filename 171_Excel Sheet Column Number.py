# https://leetcode-cn.com/problems/excel-sheet-column-number/
class Solution:
    def titleToNumber(self, s: str) -> int:
        return sum((ord(s[i]) - 64) * pow(26, len(s) - 1 - i) for i in range(len(s)))
