# https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursion
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        def buildT(in_order_list, post_order_list):
            if not in_order_list:
                return None
            if len(in_order_list) == 1:  # in_order and post_order are the same, containing only one node
                return TreeNode(in_order_list[0])
            root = TreeNode(post_order_list[-1])
            root_in_order_index = in_order_list.index(post_order_list[-1])
            left_child_in_order_list = in_order_list[:root_in_order_index]
            left_child_post_order_list = post_order_list[:root_in_order_index]
            right_child_in_order_list = in_order_list[root_in_order_index + 1:]
            right_child_post_order_list = post_order_list[root_in_order_index:-1]
            root.left = buildT(left_child_in_order_list, left_child_post_order_list)
            root.right = buildT(right_child_in_order_list, right_child_post_order_list)
            return root

        return buildT(inorder, postorder)


# stack
class Solution:
    def buildTree_pre_in(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        T = TreeNode(preorder[0])
        stack = [T]
        cur = T
        index_i = 0
        for index_p in range(1, len(preorder)):
            val_p = preorder[index_p]
            cur = stack[-1]
            if stack[-1].val == inorder[index_i]:
                # stack top has no left child, preorder[index_p] is the right child of some ancestor node of stack top
                while stack and stack[-1].val == inorder[index_i]:
                    cur = stack.pop()
                    index_i += 1
                cur.right = TreeNode(val_p)
                stack.append(cur.right)
            else:  # preorder[index_p] is the left child of stack top
                cur.left = TreeNode(val_p)
                stack.append(cur.left)
        return T

    def buildTree_pre_in_mirror(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        T = TreeNode(preorder[0])
        stack = [T]
        cur = T
        index_i = 0
        for index_p in range(1, len(preorder)):
            val_p = preorder[index_p]
            cur = stack[-1]
            if stack[-1].val == inorder[index_i]:
                # stack top has no left child, preorder[index_p] is the right child of some ancestor node of stack top
                while stack and stack[-1].val == inorder[index_i]:
                    cur = stack.pop()
                    index_i += 1
                cur.left = TreeNode(val_p)
                stack.append(cur.left)
            else:  # preorder[index_p] is the left child of stack top
                cur.right = TreeNode(val_p)
                stack.append(cur.right)
        return T

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self.buildTree_pre_in_mirror(postorder[::-1], inorder[::-1])
