# https://leetcode-cn.com/problems/string-compression/
class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n == 1:
            return 1
        cur = [chars[0], 1]
        r = 1
        w = 1
        while r < n:
            if chars[r] == cur[0]:
                cur[1] += 1
            else:
                if cur[1] > 1:
                    num2w = str(cur[1])
                    for ch in num2w:
                        chars[w] = ch
                        w += 1
                chars[w] = chars[r]
                w += 1
                cur = [chars[r], 1]
            r += 1
        if cur[1] > 1:
            num2w = str(cur[1])
            for ch in num2w:
                chars[w] = ch
                w += 1
        return w
