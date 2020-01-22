# https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string-ii/
from collections import Counter


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        cnt = Counter(s)
        while True:
            for ch in cnt:
                cnt[ch] = False
                while ch * k in s:
                    cnt[ch] = True
                    pos = s.index(ch * k)
                    s = s[:pos] + s[pos + k:]
                if not any(cnt[chh] for chh in cnt):
                    return s
