# https://leetcode-cn.com/problems/check-if-word-is-valid-after-substitutions/
class Solution:
    def isValid(self, S: str) -> bool:
        if 'abc' not in S:
            return False
        while 'abc' in S:
            pattern_pos = S.index('abc')
            S = S[:pattern_pos] + S[pattern_pos + 3:]
        if S == '':
            return True
        return False
