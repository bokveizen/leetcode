# https://leetcode-cn.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        cur = res = 0
        for t in target:
            if t > cur:
                res += t - cur
            cur = t
        return res


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = 0
        flag = True
        n = len(target)
        while flag:
            flag = False
            i = 0
            while i < n:
                while i < n and target[i] == 0:
                    i += 1
                res += i < n
                while i < n and target[i] >= 1:
                    flag = True
                    target[i] -= 1
                    i += 1
        return res
