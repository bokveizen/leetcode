# https://leetcode-cn.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sums = [0]
        threshold_k = threshold * k
        for num in arr:
            sums.append(sums[-1] + num)
        res = 0
        for i in range(len(sums) - k):
            if sums[i + k] - sums[i] >= threshold_k:
                res += 1
        return res
