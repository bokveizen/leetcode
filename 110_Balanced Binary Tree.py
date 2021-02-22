# https://leetcode-cn.com/problems/balanced-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def get_height(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            height_l = get_height(node.left)
            if height_l == -1:
                return -1
            height_r = get_height(node.right)
            if height_r == -1:
                return -1
            if abs(height_l - height_r) > 1:  # unbalanced
                return -1
            return max(height_l, height_r) + 1

        return get_height(root) != -1
