# https://leetcode-cn.com/problems/merge-sorted-array/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 == 0:
            nums1[:n] = nums2[:n]
            return
        if len2 == 0:
            return
        nums1[n:n + m] = nums1[:m]
        ptr1 = 0
        ptr2 = 0
        ptr_res = 0
        while ptr1 < m or ptr2 < n:
            # num1 = nums1[n+ptr1], num2 = nums[ptr2]
            if ptr1 == m:
                nums1[ptr_res] = nums2[ptr2]
                ptr2 += 1
            elif ptr2 == n:
                nums1[ptr_res] = nums1[n + ptr1]
                ptr1 += 1
            else:
                if nums1[n + ptr1] < nums2[ptr2]:
                    nums1[ptr_res] = nums1[n + ptr1]
                    ptr1 += 1
                else:
                    nums1[ptr_res] = nums2[ptr2]
                    ptr2 += 1
            ptr_res += 1
