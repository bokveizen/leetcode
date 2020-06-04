# https://leetcode-cn.com/problems/shortest-path-with-alternating-colors/
class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        if n == 0:
            return []
        if n == 1:
            return [0]
        if n == 2:
            return [0, 1] if [0, 1] in red_edges or [0, 1] in blue_edges else [0, -1]


