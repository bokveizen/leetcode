# https://leetcode-cn.com/problems/permutations-ii/
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        used = set()

        def backtrack(num_list, tmp_res):
            if len(tmp_res) == len(num_list):
                res.append(tmp_res)
                return
            n = len(num_list)
            for i in range(n):
                if not (i in used or (i and nums[i] == nums[i - 1] and i - 1 not in used)):
                    used.add(i)
                    backtrack(num_list, tmp_res + [num_list[i]])
                    used.remove(i)

        backtrack(nums, [])
        return res
