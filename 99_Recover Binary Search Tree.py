# https://leetcode-cn.com/problems/recover-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Using a list to restore the linear list of in-order traversal
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        in_order_linear_list = []
        ptr1 = ptr2 = None

        def in_order(root_node):
            if not root_node:
                return
            in_order(root_node.left)
            in_order_linear_list.append(root_node.val)
            in_order(root_node.right)

        def in_order_find_val(root_node, val1, val2):
            if not root_node:
                return
            in_order_find_val(root_node.left, val1, val2)
            nonlocal ptr1, ptr2
            if root_node.val == val1:
                ptr1 = root_node
            if root_node.val == val2:
                ptr2 = root_node
            in_order_find_val(root_node.right, val1, val2)

        in_order(root)
        m1 = m2 = None
        for i in range(len(in_order_linear_list) - 1):
            if in_order_linear_list[i] > in_order_linear_list[i + 1]:
                if m1 is None:
                    m1 = i
                else:
                    m2 = i + 1
        if m2 is None:
            m2 = m1 + 1
        m1 = in_order_linear_list[m1]
        m2 = in_order_linear_list[m2]
        in_order_find_val(root, m1, m2)
        ptr1.val, ptr2.val = ptr2.val, ptr1.val


# Morris traversal
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        ptr1 = ptr2 = tmp = None
        cur = root
        while cur:
            if cur.left:  # left child not empty
                # let pred be the rightmost node in the left child of the current node
                pred = cur.left
                while pred.right and pred.right != cur:
                    pred = pred.right
                if not pred.right:
                    pred.right = cur
                    cur = cur.left
                else:
                    if tmp and cur.val < tmp.val:
                        ptr2 = cur
                        if ptr1 is None:
                            ptr1 = tmp
                    tmp = cur
                    pred.right = None
                    cur = cur.right
            else:  # left child is empty
                if tmp and cur.val < tmp.val:
                    ptr2 = cur
                    if ptr1 is None:
                        ptr1 = tmp
                tmp = cur
                cur = cur.right
        ptr1.val, ptr2.val = ptr2.val, ptr1.val
