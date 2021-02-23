# https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = 0

    def sumNumbers(self, root: TreeNode) -> int:
        def helper(node, cur_sum=0):
            cur_sum = cur_sum * 10 + node.val
            if not node.left and not node.right:  # sum up at leaves
                self.sum += cur_sum
            else:
                if node.left:
                    helper(node.left, cur_sum)
                if node.right:
                    helper(node.right, cur_sum)
            return

        helper(root)
        return self.sum
