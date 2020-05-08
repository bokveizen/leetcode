# https://leetcode-cn.com/problems/intersection-of-two-linked-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        p1, p2 = headA, headB
        flag1 = flag2 = False
        found = False
        while p1 != p2:
            if p1.next:
                p1 = p1.next
            elif not flag1:
                flag1 = True
                p1 = headB
            else:
                return None
            if p2.next:
                p2 = p2.next
            elif not flag2:
                flag2 = True
                p2 = headA
        return p1


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        A_ids = set()
        tmp = headA
        while tmp:
            A_ids.add(id(tmp))
            tmp = tmp.next
        tmp = headB
        while tmp:
            if id(tmp) in A_ids:
                return tmp
            tmp = tmp.next
        return None
