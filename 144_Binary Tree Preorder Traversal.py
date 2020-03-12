# https://leetcode-cn.com/problems/binary-tree-preorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution_recursion:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def helper(root):
            if not root:
                return
            res.append(root.val)
            helper(root.left)
            helper(root.right)

        helper(root)
        return res

class Solution_iteration:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            p = stack.pop()
            res.append(p.val)
            if p.right:
                stack.append(p.right)
            if p.left:
                stack.append(p.left)
        return res

