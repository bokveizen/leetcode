# https://leetcode-cn.com/problems/restore-the-array-from-adjacent-pairs/
# from collections import *
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        if len(adjacentPairs) == 1:
            return adjacentPairs[0]
        if len(adjacentPairs) == 2:
            res = adjacentPairs[0]
            if adjacentPairs[1][0] == res[0]:
                return [adjacentPairs[1][1]] + res
            if adjacentPairs[1][0] == res[1]:
                return res + [adjacentPairs[1][1]]
            if adjacentPairs[1][1] == res[0]:
                return [adjacentPairs[1][0]] + res
            if adjacentPairs[1][1] == res[1]:
                return res + [adjacentPairs[1][0]]
        adj = dict()
        for p in adjacentPairs:
            for i in (0, 1):
                if p[i] not in adj:
                    adj[p[i]] = [p[1 - i]]
                else:
                    adj[p[i]].append(p[1 - i])
        res = None
        for v in adj:
            if len(adj[v]) == 1:
                res = [v, adj[v][0]]
                break
        while len(res) < len(adj):
            cur = res[-1]
            res += [adj[cur][0]] if adj[cur][1] == res[-2] else [adj[cur][1]]
        return res
