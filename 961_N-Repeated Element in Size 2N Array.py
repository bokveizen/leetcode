# https://leetcode-cn.com/problems/n-repeated-element-in-size-2n-array/
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        nums = []
        for i in A:
            if i not in nums:
                nums.append(i)
            else:
                return i
