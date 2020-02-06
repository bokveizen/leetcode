# https://leetcode-cn.com/problems/swap-nodes-in-pairs/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        node1 = head
        node2 = head.next
        node1.next = self.swapPairs(node2.next)
        node2.next = node1
        return node2
