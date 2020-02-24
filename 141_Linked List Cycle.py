# https://leetcode-cn.com/problems/linked-list-cycle/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        fast = head
        slow = head
        while True:
            slow = slow.next
            fast = fast.next
            if fast.next is None:
                return False
            fast = fast.next
            if fast.next is None:
                return False
            if fast == slow:
                return True
