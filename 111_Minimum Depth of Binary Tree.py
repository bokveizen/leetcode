# https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        frontier = [(root, 1)]
        while frontier:
            cur, cur_d = frontier.pop(0)
            if not cur.left and not cur.right:  # leaf
                return cur_d
            if cur.left:
                frontier.append((cur.left, cur_d + 1))
            if cur.right:
                frontier.append((cur.right, cur_d + 1))
