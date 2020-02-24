# https://leetcode-cn.com/problems/zigzag-conversion/
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s
        row_pos = []
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                row_pos.append([i])
            else:
                row_pos.append([i, 2 * numRows - 2 - i])

        def row_str(row_index):
            row = ''
            base = 0
            while row_pos[row_index][0] + base < len(s):
                for pos in row_pos[row_index]:
                    if pos + base < len(s):
                        row += s[pos + base]
                base += 2 * numRows - 2
            return row

        res = ''
        for i in range(numRows):
            res += row_str(i)
        return res
