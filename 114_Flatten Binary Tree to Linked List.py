# https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def helper(node=root):
            if not node:
                return None, None
            if not node.left and not node.right:
                return node, node
            if not node.left:
                right_head, right_end = helper(node.right)
                # node.left = None
                node.right = right_head
                return node, right_end
            if not node.right:
                left_head, left_end = helper(node.left)
                node.left = None
                node.right = left_head
                return node, left_end
            left_head, left_end = helper(node.left)
            right_head, right_end = helper(node.right)
            node.left = None
            node.right = left_head
            left_end.right = right_head
            return node, right_end

        helper()


# pred
class Solution:
    def flatten(self, root: TreeNode) -> None:
        curr = root
        while curr:
            if curr.left:
                predecessor = nxt = curr.left
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor.right = curr.right
                curr.left = None
                curr.right = nxt
            curr = curr.right
