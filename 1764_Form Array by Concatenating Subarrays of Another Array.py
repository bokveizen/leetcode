# https://leetcode-cn.com/problems/form-array-by-concatenating-subarrays-of-another-array/
class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        len_g = sum(len(g) for g in groups)
        n = len(nums)
        m = len(groups)
        if len_g > n:
            return False
        cur_g = 0
        i = 0
        while i < n:
            if len_g > n - i:
                return False
            lg = len(groups[cur_g])
            if nums[i: i + lg] == groups[cur_g]:
                cur_g += 1
                if cur_g == m:
                    return True
                len_g -= lg
                i += lg
            else:
                i += 1
