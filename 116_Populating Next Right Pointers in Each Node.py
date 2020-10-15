# https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/
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
        if not root or not root.left:
            return root

        cur_layer_head = root
        cur = root
        while cur.left:
            cur.left.next = cur.right  # connect for one node
            if cur.next:  # move to the next one in the same layer
                cur.right.next = cur.next.left
                cur = cur.next
            elif cur_layer_head.left:  # current layer finished, go to next layer
                cur_layer_head = cur_layer_head.left
                cur = cur_layer_head
        return root
