# https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Inverse of 102
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
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
        return res[::-1]
