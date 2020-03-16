# https://leetcode-cn.com/problems/compress-string-lcci/
class Solution:
    def compressString(self, S: str) -> str:
        n = len(S)
        if n <= 2:
            return S
        total_cnt = 1
        cur = S[0]
        res = ''
        cur_cnt = 1
        while total_cnt <= n:
            if total_cnt == n:
                res += cur + str(cur_cnt)
            elif S[total_cnt] != cur:
                res += cur + str(cur_cnt)
                cur = S[total_cnt]
                cur_cnt = 1
            else:
                cur_cnt += 1
            total_cnt += 1
        return res if len(res) < n else S
