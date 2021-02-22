# https://leetcode-cn.com/problems/path-sum/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == sum
        cur = collections.deque()
        cur.append((root, root.val))
        while cur:
            node, val = cur.popleft()
            if not node.left and not node.right and val == sum:
                return True
            if node.left:
                cur.append((node.left, val + node.left.val))
            if node.right:
                cur.append((node.right, val + node.right.val))
        return False
