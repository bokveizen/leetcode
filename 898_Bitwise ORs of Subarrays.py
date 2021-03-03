# https://leetcode-cn.com/problems/bitwise-ors-of-subarrays/
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 1
        res = {arr[0]}
        cur = {arr[0]}
        for i in range(1, n):
            cur = {arr[i] | c for c in cur} | {arr[i]}
            res.update(cur)
            # cur = new
        return len(res)
