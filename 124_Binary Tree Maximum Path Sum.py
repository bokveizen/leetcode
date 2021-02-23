# https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.cur_sum = -30000000

    def maxPathSum(self, root: TreeNode) -> int:
        def helper(node):
            if not node:
                return 0
            left = max(helper(node.left), 0)
            right = max(helper(node.right), 0)
            self.cur_sum = max(self.cur_sum, node.val + left + right)
            return node.val + max(left, right)
        helper(root)
        return self.cur_sum
