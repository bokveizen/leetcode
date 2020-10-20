# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        def levelO(root_node):
            if not root_node:
                return []
            res = [[root_node.val]]
            left = levelO(root_node.left)
            right = levelO(root_node.right)
            height_l = len(left)
            height_r = len(right)
            for i in range(max(height_l, height_r)):
                if i < height_l and i < height_r:
                    if left[i] + right[i]:
                        res.append(left[i] + right[i])
                elif i >= height_l:
                    if right[i]:
                        res.append(right[i])
                else:
                    if left[i]:
                        res.append(left[i])
            return res

        return levelO(root)

# BFS-like
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = [root]
        while q:
            cur_level = []
            len_q = len(q)
            for _ in range(len_q):
                cur = q.pop(0)
                cur_level.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(cur_level)
        return res

