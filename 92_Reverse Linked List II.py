# https://leetcode-cn.com/problems/reverse-linked-list-ii/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        dummy = ListNode(0)
        dummy.next = head
        tmp1 = dummy
        for _ in range(m - 1):
            tmp1 = tmp1.next
        # if n == m + 1:
        #     first = tmp1.next
        #     second = first.next
        #     tmp1.next = second
        #     first.next = second.next
        #     second.next = first
        # else:
        pre = tmp1.next
        cur = tmp1.next.next
        # nxt = tmp1.next.next.next
        for _ in range(n - m):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        tmp1.next.next = cur
        tmp1.next = pre
        return dummy.next
