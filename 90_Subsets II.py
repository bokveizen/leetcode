# https://leetcode-cn.com/problems/subsets-ii/
from collections import Counter


class Solution:
    def subsetsWithDup(self, nums):
        if not nums:
            return []
        res = []
        c = Counter(nums)
        n = len(c)
        # print('n', n)
        candidates = [[num] for num in c]
        # print('candidates', candidates)
        upper_bounds = [c[num] for num in c]
        # print('upper_bounds', upper_bounds)
        iteration_index = []
        i = 0
        while True:
            if i == n:
                break
            if i == 0:
                iteration_index = [[j] for j in range(upper_bounds[i] + 1)]
            else:
                iteration_index_new = [old + [new] for old in iteration_index for new in range(upper_bounds[i] + 1)]
                iteration_index = iteration_index_new
            i += 1
        # print(iteration_index)
        for ii in iteration_index:
            ite_res = []
            for candidate_index in range(n):
                ite_res += candidates[candidate_index] * ii[candidate_index]
            res.append(ite_res)
        # print(res)
        return res

