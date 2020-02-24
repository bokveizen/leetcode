# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k <= 1:
            return head
        # less than k nodes
        # current = head
        # for i in range(k - 1):
        #     if not (current and current.next):
        #         return head
        #     current = current.next
        if not head:
            return head
        nodes = [head]
        # node1 = head
        # node2 = node1.next
        # ...
        # nodek = nodek-1.next
        for i in range(k - 1):
            if not nodes[-1].next:
                return head
            nodes.append(nodes[-1].next)
        # node1.next = self.reverseKGroup(nodek.next)
        # node2.next = node1
        # ...
        # nodek.next = nodek-1
        nodes[0].next = self.reverseKGroup(nodes[-1].next, k)
        for i in range(k - 1):
            nodes[i + 1].next = nodes[i]
        return nodes[-1]
