# https://leetcode-cn.com/problems/4sum-ii/
from typing import List
import collections


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        h = collections.Counter(-a - b for a in A for b in B)
        res = sum([h[c + d] for c in C for d in D])
        return res
