# https://leetcode-cn.com/problems/valid-number/
class Solution:
    def isNumber(self, s: str) -> bool:
        valid_chars = '0123456789e+-.'
        # del spaces
        while s and s[0] == ' ':
            s = s[1:]
        while s and s[-1] == ' ':
            s = s[:-1]
        # some special cases
        if (not s) or (' ' in s):
            return False
        for char in s:
            if char not in valid_chars:
                return False

        def isPureNumber(num_s, for_order=False):
            # check sign
            if num_s[0] == '+' or num_s[0] == '-':
                num_s = num_s[1:]
            # num_s should be unsigned number
            if not num_s or '+' in num_s or '-' in num_s:
                return False
            if '.' in num_s:
                if for_order:
                    return False
                int_p, dec_p = num_s.split('.', 1)
                if (not int_p and not dec_p) or '.' in int_p or '.' in dec_p:
                    return False
            return True

        # no space, all valid chars
        if 'e' in s:
            sig, order = s.split('e', 1)
            if not sig or not order or 'e' in sig or 'e' in order:
                return False
            # only 1 e
            return isPureNumber(sig) and isPureNumber(order, True)
        return isPureNumber(s)
