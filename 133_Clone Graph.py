# https://leetcode-cn.com/problems/clone-graph/
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # special cases
        if not node:
            return None
        if not node.neighbors:
            return Node(1)
        res = Node(1, [Node() for _ in node.neighbors])
        created = {1: res}
        over = set()
        queue = [node]
        while queue:
            cur = queue.pop(0)
            cur_copy = created[cur.val]
            for i in range(len(cur.neighbors)):
                new_val = cur.neighbors[i].val
                if new_val not in created:
                    new_node = Node(new_val, [Node() for _ in cur.neighbors[i].neighbors])
                    created[new_val] = new_node
                else:
                    new_node = created[new_val]
                cur_copy.neighbors[i] = new_node
                if new_val not in over:
                    queue.append(cur.neighbors[i])
            over.add(cur.val)
        return res

# DFS
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        lookup = {}

        def dfs(node):
            # print(node.val)
            if not node: return
            if node in lookup:
                return lookup[node]
            clone = Node(node.val, [])
            lookup[node] = clone
            for n in node.neighbors:
                clone.neighbors.append(dfs(n))

            return clone

        return dfs(node)


# BFS
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        from collections import deque
        lookup = {}

        def bfs(node):
            if not node: return
            clone = Node(node.val, [])
            lookup[node] = clone
            queue = deque()
            queue.appendleft(node)
            while queue:
                tmp = queue.pop()
                for n in tmp.neighbors:
                    if n not in lookup:
                        lookup[n] = Node(n.val, [])
                        queue.appendleft(n)
                    lookup[tmp].neighbors.append(lookup[n])
            return clone

        return bfs(node)
