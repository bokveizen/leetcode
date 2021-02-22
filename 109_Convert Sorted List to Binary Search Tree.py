# https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:  # Q108
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])

        def recur(left=0, right=len(nums) - 1):
            if left > right:
                return None
            mid = (left + right) >> 1
            root = TreeNode(nums[mid])
            root.left = recur(left, mid - 1)
            root.right = recur(mid + 1, right)
            return root

        return recur()

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return self.sortedArrayToBST(nums)


# fast and slow pointers
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        pre = head
        p = pre.next
        q = p.next
        # find midpoint = p
        while q and q.next:
            pre = pre.next
            p = pre.next
            q = q.next.next
        pre.next = None
        return TreeNode(val=p.val, left=self.sortedListToBST(head), right=self.sortedListToBST(p.next))



