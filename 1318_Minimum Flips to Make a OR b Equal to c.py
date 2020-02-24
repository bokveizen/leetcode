# https://leetcode-cn.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a_bin = format(a, 'b')
        b_bin = format(b, 'b')
        c_bin = format(c, 'b')
        max_bin_len = max(len(bin_str) for bin_str in [a_bin, b_bin, c_bin])
        format_code = '0' + str(max_bin_len) + 'b'
        a_bin, b_bin, c_bin = format(a, format_code), format(b, format_code), format(c, format_code)
        res = 0
        for i in range(max_bin_len):
            if int(a_bin[i]) | int(b_bin[i]) == int(c_bin[i]):
                continue
            elif c_bin[i] == '1':
                res += 1
            else:
                res += int(a_bin[i]) + int(b_bin[i])
        return res

