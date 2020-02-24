# https://leetcode-cn.com/problems/friend-circles/
from typing import List


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        # union find
        # init.
        parent_list = [i for i in range(len(M))]

        def root(x):
            pos = x
            while parent_list[pos] != pos:
                pos = parent_list[pos]
            return pos

        def union(x1, x2):
            if root(x1) != root(x2):
                parent_list[root(x1)] = root(x2)
                return 1
            return 0

        res = len(M)
        for i in range(len(M)):
            for j in range(i):
                if M[i][j]:
                    res -= union(i, j)
        return res
