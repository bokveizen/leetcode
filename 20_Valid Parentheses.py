# https://leetcode-cn.com/problems/valid-parentheses/
from collections import Counter


class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        if len(s) % 2:
            return False
        if s[0] not in '([{' or s[-1] not in ')]}':
            return False
        cnt = Counter(s)
        if cnt['('] != cnt[')'] or cnt['['] != cnt[']'] or cnt['{'] != cnt['}']:
            return False
        while '()' in s or '{}' in s or '[]' in s:
            while '()' in s:
                par_pos = s.index('()')
                s = s[:par_pos] + s[par_pos + 2:]
            while '[]' in s:
                par_pos = s.index('[]')
                s = s[:par_pos] + s[par_pos + 2:]
            while '{}' in s:
                par_pos = s.index('{}')
                s = s[:par_pos] + s[par_pos + 2:]
        return s == ''
