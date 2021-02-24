# https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.val_sum = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        def helper(root):
            if not root:
                return
            helper(root.right)
            self.val_sum += root.val
            root.val = self.val_sum
            helper(root.left)

        helper(root)
        return root
