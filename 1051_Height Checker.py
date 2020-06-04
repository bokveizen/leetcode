# https://leetcode-cn.com/problems/height-checker/
from collections import Counter


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        cnt = Counter(heights)
        cur = 0
        res = 0
        for num in sorted(cnt.keys()):
            for i in range(cur, cur + cnt[num]):
                if heights[i] != num:
                    res += 1
            cur += cnt[num]
        return res
