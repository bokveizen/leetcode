# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        new_head = ListNode(-1)
        new_head.next = head
        pre = new_head
        cur = head
        while pre and cur and cur.next:  # at least satisfied for once (head and head.next)
            if cur.val != cur.next.val:
                pre = cur
                cur = cur.next
            else:  # cur = cur.next
                cur_var = cur.val
                tmp = cur.next
                last_num = False
                while tmp.val == cur_var:
                    if not tmp.next:
                        last_num = True
                        break
                    else:
                        tmp = tmp.next
                if last_num:  # END
                    pre.next = None
                    break
                else:
                    pre.next = tmp
                    cur = tmp
        return new_head.next
