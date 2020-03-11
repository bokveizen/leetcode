# https://leetcode-cn.com/problems/diameter-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 1

        def depth(node):
            if not node:
                return 0
            L = depth(node.left)
            R = depth(node.right)
            nonlocal res
            if L + R + 1 > res:
                res = L + R + 1
            return L + 1 if L > R else R + 1

        depth(root)
        return res - 1
