# https://leetcode-cn.com/problems/super-washing-machines/
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        n = len(machines)
        if n == 1:
            return 0
        total_dresses_num = sum(machines)
        if total_dresses_num % n:
            return -1
        diff = [m - total_dresses_num // n for m in machines]
        res = 0
        pre_sum = 0
        max_pre_sum_abs = 0
        for d in diff:
            pre_sum += d
            max_pre_sum_abs = max(max_pre_sum_abs, abs(pre_sum))
            res = max(res, max_pre_sum_abs, d)
        return res
