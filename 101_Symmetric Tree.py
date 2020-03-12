# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    #     if not p and not q:
    #         return True
    #     elif not p or not q:
    #         return False
    #     if p.val != q.val:
    #         return False
    #     else:
    #         return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSymmetricTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        if p.val != q.val:
            return False
        else:
            return self.isSymmetricTree(p.left, q.right) and self.isSymmetricTree(p.right, q.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        # if not root.left and not root.right:
        #     return True
        # if not root.left or not root.right:
        #     return False
        # root.left and root.right
        return self.isSymmetricTree(root.left, root.right)
