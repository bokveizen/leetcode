# https://leetcode-cn.com/problems/path-sum-ii/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        if not root.left and not root.right:
            return [[sum]] if root.val == sum else []
        res = []
        cur = collections.deque()
        cur.append((root, [root.val], root.val))
        while cur:
            node, path, path_sum = cur.popleft()
            if not node.left and not node.right and path_sum == sum:
                res.append(path)
            if node.left:
                cur.append((node.left, path + [node.left.val], path_sum + node.left.val))
            if node.right:
                cur.append((node.right, path + [node.right.val], path_sum + node.right.val))
        return res
