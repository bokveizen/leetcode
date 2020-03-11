# https://leetcode-cn.com/problems/partition-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        before = before_head = ListNode('-')
        after = after_head = ListNode('-')
        tmp = head
        while tmp:
            if tmp.val < x:
                before.next = tmp
                before = before.next
            else:
                after.next = tmp
                after = after.next
            tmp = tmp.next
        after.next = None
        before.next = after_head.next
        return before_head.next
