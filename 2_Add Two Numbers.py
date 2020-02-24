# https://leetcode-cn.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        carry = 0
        current_node = res
        if not l1 and not l2:
            return None
        while True:
            l1_val = 0 if not l1 else l1.val
            l2_val = 0 if not l2 else l2.val
            current_digit = (l1_val + l2_val + carry) % 10
            carry = (l1_val + l2_val + carry) // 10
            current_node.val = current_digit
            if (l1 and l1.next) or (l2 and l2.next):
                current_node.next = ListNode(0)
                current_node = current_node.next
                l1 = None if not l1 else l1.next
                l2 = None if not l2 else l2.next
            elif not carry:
                return res
            else:
                current_node.next = ListNode(1)
                return res
