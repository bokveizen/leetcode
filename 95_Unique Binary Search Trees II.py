# https://leetcode-cn.com/problems/unique-binary-search-trees-ii/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        dp = [[] for i in range(n + 1)]
        dp[0] = [None]

        def tree_add(root, add_val):
            if not root:
                return None
            new = TreeNode(val=root.val + add_val)
            new.left = tree_add(root.left, add_val)
            new.right = tree_add(root.right, add_val)
            return new

        for i in range(1, n + 1):
            for j in range(1, i + 1):
                for left_tree in dp[j - 1]:
                    for right_tree in dp[i - j]:
                        # root = i, left = left_tree, right = right_tree + i
                        dp[i].append(TreeNode(val=j, left=left_tree, right=tree_add(right_tree, j)))
        return dp[-1]
