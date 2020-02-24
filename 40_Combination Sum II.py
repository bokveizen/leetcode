# https://leetcode-cn.com/problems/combination-sum-ii/
from collections import Counter


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
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
        cnt = Counter(candidates)
        candidates_list = sorted(list(cnt))
        n = len(candidates_list)

        def backtrack(i, i_time, tmp_sum, tmp_res):
            i_time_total = cnt[candidates_list[i]]
            if tmp_sum > target:
                return
            if tmp_sum == target:
                res.append(tmp_res)
                return
            # tmp_sum < tgt
            for j in range(i, n):
                if j == i:
                    if i_time >= i_time_total:  # used out
                        continue
                    else:  # candidates_list[i] still available
                        if tmp_sum + candidates_list[i] > target:
                            break
                        backtrack(i, i_time + 1, tmp_sum + candidates_list[i], tmp_res + [candidates_list[i]])
                else:
                    if tmp_sum + candidates_list[j] > target:
                        break
                    backtrack(j, 1, tmp_sum + candidates_list[j], tmp_res + [candidates_list[j]])

        backtrack(0, 0, 0, [])
        return res
