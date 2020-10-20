# https://leetcode-cn.com/problems/reorder-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        len = 1
        tmp = head
        while tmp.next:
            tmp = tmp.next
            len += 1
        if len <= 2:
            return
        tmp = head
        for _ in range(len//2):
            tmp = tmp.next
        nxt = tmp.next
        tmp.next = None
        while nxt.next:
            nnxt = nxt.next
            nxt.next = tmp
            tmp = nxt
            nxt = nnxt
        nxt.next = tmp
        tmp = head
        for i in range(len//2 - 1):
            tmp_next = tmp.next
            nxt_prev = nxt.next
            tmp.next = nxt
            nxt.next = tmp_next
            tmp = tmp_next
            nxt = nxt_prev
        tmp.next = nxt
