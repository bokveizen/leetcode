# https://leetcode-cn.com/problems/combination-sum/
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        if target == 1:
            return [[1]] if 1 in candidates else []
        res = []
        if target in candidates:
            res = [[target]]
        candidates = [candidate for candidate in candidates if candidate < target]
        if not candidates:
            return res
        candidates.sort()
        n = len(candidates)

        def backtrack(i, tmp_sum, tmp_res):
            if tmp_sum > target:
                return
            if tmp_sum == target:
                res.append(tmp_res)
                return
            for j in range(i, n):
                if tmp_sum + candidates[j] > target:
                    break
                backtrack(j, tmp_sum + candidates[j], tmp_res + [candidates[j]])

        backtrack(0, 0, [])
        return res

