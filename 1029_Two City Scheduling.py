# https://leetcode-cn.com/problems/two-city-scheduling/
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        cost_sum_a = sum(costs[i][0] for i in range(n))
        diffs = sorted(costs[i][1] - costs[i][0] for i in range(n))
        for i in range(n, 2 * n):
            cost_a, cost_b = costs[i]
            cost_sum_a += cost_a
            if cost_b - cost_a < diffs[-1]:
                diffs.pop()
                diffs.append(cost_b - cost_a)
                diffs.sort()
        return cost_sum_a + sum(diffs)
