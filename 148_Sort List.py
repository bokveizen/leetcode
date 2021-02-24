# https://leetcode-cn.com/problems/sort-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def helper(h=head, t=None):
            if not h:
                return h
            if h.next == t:
                h.next = None
                return h
            # dummy = ListNode(next=h)
            fast = slow = h
            while fast != t:
                slow = slow.next
                fast = fast.next
                if fast != t:
                    fast = fast.next
            # m = slow
            return merge(helper(h, slow), helper(slow, t))

        def merge(p1, p2):
            dummy = ListNode()
            cur, cur1, cur2 = dummy, p1, p2
            while cur1 and cur2:
                if cur1.val < cur2.val:
                    cur.next = cur1
                    cur1 = cur1.next
                else:
                    cur.next = cur2
                    cur2 = cur2.next
                cur = cur.next
            if cur1:
                cur.next = cur1
            elif cur2:
                cur.next = cur2
            return dummy.next

        return helper()


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(head1: ListNode, head2: ListNode) -> ListNode:
            dummyHead = ListNode(0)
            temp, temp1, temp2 = dummyHead, head1, head2
            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            if temp1:
                temp.next = temp1
            elif temp2:
                temp.next = temp2
            return dummyHead.next

        if not head:
            return head

        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        dummyHead = ListNode(0, head)
        subLength = 1
        while subLength < length:
            prev, curr = dummyHead, dummyHead.next
            while curr:
                head1 = curr
                for i in range(1, subLength):
                    if curr.next:
                        curr = curr.next
                    else:
                        break
                head2 = curr.next
                curr.next = None
                curr = head2
                for i in range(1, subLength):
                    if curr and curr.next:
                        curr = curr.next
                    else:
                        break

                succ = None
                if curr:
                    succ = curr.next
                    curr.next = None

                merged = merge(head1, head2)
                prev.next = merged
                while prev.next:
                    prev = prev.next
                curr = succ
            subLength <<= 1

        return dummyHead.next


# linked list merging in C++
# struct Node {
#     Node* next;
#     int val;
# };
#
# Node* merge(Node* a, Node* b) {
#     Node fake_head(nullptr, 0);
#
#     Node* cur = &fake_head;
#     while (a && b) {
#         if (a->val < b->val) { cur->next = a; a = a->next; }
#         else                 { cur->next = b; b = b->next; }
#         cur = cur->next;
#     }
#
#     cur->next = a ? a : b;
#     return fake_head.next;
# }
