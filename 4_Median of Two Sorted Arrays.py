# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1:
            return nums2[len(nums2) // 2] if len(nums2) % 2 \
                else (nums2[len(nums2) // 2] + nums2[len(nums2) // 2 - 1]) / 2
        if not nums2:
            return nums1[len(nums1) // 2] if len(nums1) % 2 \
                else (nums1[len(nums1) // 2] + nums1[len(nums1) // 2 - 1]) / 2
        # make sure nums1 if the shorter one
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        odd = (len(nums1) + len(nums2)) % 2
        half = (len(nums1) + len(nums2)) // 2

        def med_check(k):
            if k == 0:
                if nums2[half - k - 1] <= nums1[0]:
                    if odd:
                        med = min(nums1[0], nums2[half - k])
                    else:
                        med_l = nums2[half - k - 1]
                        if half - k < len(nums2):
                            med_r = min(nums2[half - k], nums1[0])
                        else:
                            med_r = nums1[0]
                        med = (med_l + med_r) / 2
                    return True, med
                else:
                    return False, 0
            elif k == len(nums1):
                if nums1[-1] <= nums2[half - k]:
                    if odd:
                        med = nums2[half - k]
                    else:
                        med_r = nums2[half - k]
                        if half - k == 0:
                            med_l = nums1[-1]
                        else:
                            med_l = max(nums1[-1], nums2[half - k - 1])
                        med = (med_l + med_r) / 2
                    return True, med
                else:
                    return False, 0
            else:
                if nums1[k - 1] <= nums2[half - k] and nums2[half - k - 1] <= nums1[k]:
                    if odd:
                        med = min(nums1[k], nums2[half - k])
                    else:
                        med_l = max(nums1[k - 1], nums2[half - k - 1])
                        med_r = min(nums1[k], nums2[half - k])
                        med = (med_l + med_r) / 2
                    return True, med
                else:
                    return False, -1 if nums1[k - 1] > nums2[half - k] else 1

        k_lower = 0
        k_upper = len(nums1)
        while k_lower <= k_upper:
            if k_lower >= k_upper - 1:
                return med_check(k_lower)[1] if med_check(k_lower)[0] else med_check(k_upper)[1]
            else:
                k = (k_lower + k_upper) // 2
                if med_check(k)[0]:
                    return med_check(k)[1]
                elif med_check(k)[1] == -1:
                    k_upper = k - 1
                else:
                    k_lower = k + 1
