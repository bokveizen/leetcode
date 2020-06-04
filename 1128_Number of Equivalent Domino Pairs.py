from collections import defaultdict
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        if len(dominoes) < 2:
            return 0
        d = defaultdict(int)
        for domino in dominoes:
            key = tuple(sorted(domino))
            d[key] += 1
        if not d.items():
            return 0
        else:
            return sum(a[1] * (a[1] - 1) // 2 for a in d.items())
