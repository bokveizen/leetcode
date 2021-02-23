# https://leetcode-cn.com/problems/linked-list-cycle-ii/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return None
        fast = head
        slow = head
        while True:
            slow = slow.next
            fast = fast.next
            if fast.next is None:
                return None
            fast = fast.next
            if fast.next is None:
                return None
            if fast == slow:
                break
        fast = head
        while True:
            if fast == slow:
                return slow
            slow = slow.next
            fast = fast.next
