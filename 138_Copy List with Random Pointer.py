# https://leetcode-cn.com/problems/copy-list-with-random-pointer/
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        new_head = Node(head.val)
        cur = head
        nxt = cur.next
        cur_new = new_head
        while nxt:
            cur.next = cur_new
            if cur.random:
                cur_new.random = cur.random
            cur = nxt
            nxt = nxt.next
            nxt_new = Node(cur.val)
            cur_new.next = nxt_new
            cur_new = nxt_new
        cur.next = cur_new
        if cur.random:
            cur_new.random = cur.random

        cur_new = new_head
        while cur_new:
            if cur_new.random:
                cur_new.random = cur_new.random.next
            cur_new = cur_new.next

        return new_head
