# https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])

        def recur(left=0, right=len(nums) - 1):
            if left > right:
                return None
            mid = (left + right) >> 1
            root = TreeNode(nums[mid])
            root.left = recur(left, mid - 1)
            root.right = recur(mid + 1, right)
            return root

        return recur()
