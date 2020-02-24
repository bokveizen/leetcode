# https://leetcode-cn.com/problems/play-with-chips/
class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        return sum([i % 2 for i in chips]) if sum([i % 2 for i in chips]) <= len(chips) // 2 \
            else len(chips) - sum([i % 2 for i in chips])