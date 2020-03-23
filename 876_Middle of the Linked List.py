# https://leetcode-cn.com/problems/middle-of-the-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # if not head.next:
        #     return head
        first = head
        second = head
        while True:
            if not second.next:
                return first
            if second.next and not second.next.next:
                return first.next
            first = first.next
            second = second.next.next

