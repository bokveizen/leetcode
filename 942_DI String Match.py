# https://leetcode-cn.com/problems/di-string-match/
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        # if len(S) == 1:
        #     return [0, 1] if S == 'I' else [1, 0]
        if all(c == 'I' for c in S):
            return list(range(len(S) + 1))
        if all(c == 'D' for c in S):
            return list(reversed(list(range(len(S) + 1))))
        res = []
        upper = len(S) + 1
        lower = -1
        if S[0] == 'I':
            res.append(0)
            lower = 0
        else:
            res.append(len(S))
            upper = len(S)
        for i in range(1, len(S)):
            if S[i] == 'I':
                res.append(lower + 1)
                lower += 1
            else:
                res.append(upper - 1)
                upper -= 1
        res.append(lower + 1)
        return res


