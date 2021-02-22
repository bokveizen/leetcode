# https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        cur = root
        next_layer_cur = next_layer_head = None
        while cur:
            # connection from the previous brother's children and between own children
            if cur.left:
                if not next_layer_head:
                    next_layer_cur = next_layer_head = cur.left
                else:
                    next_layer_cur.next = cur.left
                    next_layer_cur = next_layer_cur.next
            if cur.right:
                if not next_layer_head:
                    next_layer_cur = next_layer_head = cur.right
                else:
                    next_layer_cur.next = cur.right
                    next_layer_cur = next_layer_cur.next

            # move to the next one in the same layer
            if cur.next:
                cur = cur.next

            # current layer finished, go to next layer
            else:
                cur = next_layer_head
                next_layer_cur = next_layer_head = None

        return root
