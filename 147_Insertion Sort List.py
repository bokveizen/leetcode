# https://leetcode-cn.com/problems/insertion-sort-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        dummy = ListNode()
        dummy.next = head
        last = head
        cur = head.next
        while cur:
            if cur.val >= last.val:  # already sorted
                last = cur
                cur = cur.next
            else:  # cur.val < last.val
                tmp = dummy
                while True:
                    if tmp.next.val >= cur.val:
                        last.next = cur.next
                        cur.next = tmp.next
                        tmp.next = cur
                        break
                    tmp = tmp.next
                cur = last.next
        return dummy.next
