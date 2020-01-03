# https://leetcode-cn.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        sym_val_dict = {'I': 1,
                        'V': 5,
                        'X': 10,
                        'L': 50,
                        'C': 100,
                        'D': 500,
                        'M': 1000}
        n = len(s)
        if n == 0:
            return 0
        if n == 1:
            return sym_val_dict[s[0]]
        res = 0
        i = 0
        while True:
            if i > n - 1:
                return res
            cur = s[i]
            if i == n - 1:
                res += sym_val_dict[cur]
                return res
            nxt = s[i + 1]
            if cur == nxt:
                res += 2 * sym_val_dict[cur]
                i += 2
            elif sym_val_dict[cur] > sym_val_dict[nxt]:
                res += sym_val_dict[cur]
                i += 1
            else:
                res += sym_val_dict[nxt] - sym_val_dict[cur]
                i += 2
