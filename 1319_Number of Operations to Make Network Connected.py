# https://leetcode-cn.com/problems/number-of-operations-to-make-network-connected/
class UnionFind:
    def __init__(self, n: int):
        self.roots = list(range(n))
        self.sizes = [1] * n
        self.n = n
        # for this problem
        self.set_count = n

    def findset(self, x: int) -> int:
        if self.roots[x] == x:
            return x
        self.roots[x] = self.findset(self.roots[x])
        return self.roots[x]

    def unite(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        if x == y:
            return False
        if self.sizes[x] < self.sizes[y]:
            x, y = y, x
        self.roots[y] = x
        self.sizes[x] += self.sizes[y]
        self.set_count -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        return x == y


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        uf = UnionFind(n)
        for x, y in connections:
            uf.unite(x, y)

        return uf.set_count - 1
