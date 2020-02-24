# https://leetcode-cn.com/problems/sum-of-root-to-leaf-binary-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        ans = 0

        def f(r, s):
            if r:
                s = (s << 1) + r.val
                if not r.left and not r.right:  # leaf
                    nonlocal ans
                    ans += s
                else:
                    f(r.left, s)
                    f(r.right, s)

        f(root, 0)
        return ans
