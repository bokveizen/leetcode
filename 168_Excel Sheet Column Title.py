# https://leetcode-cn.com/problems/excel-sheet-column-title/
class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ''
        while n:
            res = chr(65 + (n - 1) % 26) + res
            n = (n - 1) // 26
        return res
