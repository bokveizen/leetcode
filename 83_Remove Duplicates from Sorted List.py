# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        cur = head
        while cur.next:
            if cur.next.val != cur.val:
                cur = cur.next
            else:
                tmp = cur.next
                while tmp.val == cur.val:
                    if not tmp.next:
                        cur.next = None
                        return head
                    else:
                        tmp = tmp.next
                cur.next = tmp
                cur = tmp
        return head
