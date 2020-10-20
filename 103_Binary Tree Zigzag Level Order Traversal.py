# https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque([root])
        left_to_right = True
        while q:
            cur_level = []
            len_q = len(q)
            for _ in range(len_q):
                if left_to_right:
                    cur = q.popleft()
                    cur_level.append(cur.val)
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
                else:
                    cur = q.pop()
                    cur_level.append(cur.val)
                    if cur.right:
                        q.appendleft(cur.right)
                    if cur.left:
                        q.appendleft(cur.left)
            res.append(cur_level)
            left_to_right = not left_to_right
        return res
