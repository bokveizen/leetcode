# https://leetcode-cn.com/problems/maximum-level-sum-of-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        cur_max = (1, root.val)
        cur_nodes = [root]
        cur_lvl = 1
        while cur_nodes:
            tmp_nodes = []
            tmp_val = 0
            while cur_nodes:    
                node = cur_nodes.pop()
                if node.left:
                    tmp_val += node.left.val
                    tmp_nodes.append(node.left)
                if node.right:
                    tmp_val += node.right.val
                    tmp_nodes.append(node.right)
            if tmp_nodes and tmp_val > cur_max[1]:
                    cur_max = (cur_lvl + 1, tmp_val)
            cur_nodes = tmp_nodes
            cur_lvl += 1
        return cur_max[0]