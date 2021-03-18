# https://leetcode-cn.com/problems/loud-and-rich/
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        if not richer:
            return list(range(n))
        res = [-1] * n
        r = dict()
        for x, y in richer:
            if y not in r:
                r[y] = {x}
            else:
                r[y].add(x)

        def helper(j):
            if res[j] != -1:
                return res[j]
            if j not in r:
                res[j] = j
                return j
            a = j
            for v in r[j]:
                if quiet[helper(v)] < quiet[a]:
                    a = helper(v)
            res[j] = a
            return a

        for i in range(n):
            helper(i)

        return res
