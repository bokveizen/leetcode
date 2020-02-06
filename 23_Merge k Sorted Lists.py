# https://leetcode-cn.com/problems/merge-k-sorted-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not (l1 and l2):
            return l1 or l2
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l2.next, l1)
            return l2

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        # tmp = lists
        # while len(tmp) != 1:
        #     if len(tmp) % 2:
        #         tmp.append(None)
        #     new_tmp = []
        #     for i in range(len(tmp) // 2):
        #         new_tmp.append(self.mergeTwoLists(tmp[2 * i], tmp[2 * i + 1]))
        #     tmp = new_tmp
        # return tmp[0]
        k = len(lists)
        if k % 2:
            lists.append(None)
            k += 1
        while k != 1:
            if k % 2:
                lists[k] = None
                k += 1
            for i in range(k // 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[k - i - 1])
            k //= 2
        return lists[0]
