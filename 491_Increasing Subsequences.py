# https://leetcode-cn.com/problems/increasing-subsequences/
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 2:
            return []
        if n == 2:
            return [nums] if nums[1] >= nums[0] else []

        # first solution (really slow)
        # res = set()
        #
        # def backtrack(cur, last_pos):
        #     if last_pos == n - 1:
        #         if len(cur) >= 2:
        #             res.add(tuple(cur))
        #         return
        #     for i in range(last_pos + 1, n):
        #         if nums[i] >= cur[-1]:
        #             backtrack(cur + [nums[i]], i)
        #             backtrack(cur, i)
        #         elif i == n - 1 and len(cur) >= 2:
        #             res.add(tuple(cur))
        #
        # for i in range(n - 1):
        #     backtrack([nums[i]], i)
        # return [list(e) for e in res]

        # DP
        # res_set = {(nums[0],)}
        # for i in range(1, n):
        #     num = nums[i]
        #     res_set.update({j + (num,) for j in res_set if j[-1] <= num})
        #     res_set.add((i,))
        # return [list(i) for i in res_set if len(i) > 1]

        # DFS
        res = []

        def dfs(cur_pos=0, tmp=None):
            if tmp is None:
                tmp = []
            if len(tmp) >= 2:
                res.append(tmp)
            used = set()
            for i in range(cur_pos, n):
                num = nums[i]
                if num in used:
                    continue
                if not tmp or num >= tmp[-1]:
                    used.add(num)
                    dfs(i + 1, tmp + [num])

        dfs()
        return res
