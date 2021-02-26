# https://leetcode-cn.com/problems/defuse-the-bomb/
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0 for _ in code]
        n = len(code)
        res = []
        if k > 0:
            cur = sum(code[1:1 + k])
            res.append(cur)
            for i in range(1, n):
                cur = cur - code[i] + code[(i + k) % n]
                res.append(cur)
        else:
            cur = sum(code[-1 + k: -1])
            res.append(cur)
            for i in range(n - 2, -1, -1):
                cur = cur - code[i] + code[(i + k + n) % n]
                res = [cur] + res
        return res
