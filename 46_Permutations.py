# https://leetcode-cn.com/problems/permutations/
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(num_list, tmp_res):
            if not num_list:
                res.append(tmp_res)
                return
            n = len(num_list)
            for i in range(n):
                backtrack(num_list[:i] + num_list[i + 1:], tmp_res + [num_list[i]])

        backtrack(nums, [])
        return res
