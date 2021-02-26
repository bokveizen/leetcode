from functools import lru_cache


# https://leetcode-cn.com/problems/all-possible-full-binary-trees/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if not N % 2:
            return []

        @lru_cache
        def helper(n=N):
            if n == 1:
                return [TreeNode(0)]
            res = []
            for i in range(1, n - 1, 2):
                for lc in helper(i):
                    for rc in helper(n - 1 - i):
                        T = TreeNode(0)
                        T.left = lc
                        T.right = rc
                        res.append(T)
            return res

        return helper()
