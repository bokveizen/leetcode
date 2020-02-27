# https://leetcode-cn.com/problems/rotate-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head

        # make a circle
        tmp = head
        n = 1
        while tmp.next:
            tmp = tmp.next
            n += 1
        tmp.next = head

        tmp = head
        k %= n
        for _ in range(n - 1 - k):
            tmp = tmp.next
        new_head = tmp.next
        tmp.next = None
        return new_head
