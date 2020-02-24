# https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters/
from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s:
            return 0
        s_cnt = Counter(s)
        if max(s_cnt[i] for i in s_cnt) < k:
            return 0
        if min(s_cnt[i] for i in s_cnt) >= k:
            return len(s)
        t = min(s_cnt, key=lambda x: s_cnt[x])
        return max(self.longestSubstring(a, k) for a in s.split(t))
