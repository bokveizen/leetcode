# https://leetcode-cn.com/problems/gas-station/
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if n == 0:
            return -1
        if n == 1:
            return 0 if gas[0] >= cost[0] else -1
        # if sum(cost) > sum(gas):
        #     return -1

        cur = 0
        start = 0
        total = 0
        for i in range(n):
            cur += gas[i] - cost[i]
            if cur < 0:
                start = i + 1
                cur = 0
            total += gas[i] - cost[i]
        return start if total >= 0 else -1


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if n == 0:
            return -1
        if n == 1:
            return 0 if gas[0] >= cost[0] else -1
        if sum(cost) > sum(gas):
            return -1
        dif = [gas[i] - cost[i] for i in range(n)]
        for i in range(n):
            if dif[i] <= 0:
                continue
            res = dif[i]
            cnt = 1
            idx = (i + 1) % n
            while cnt < n:
                res += dif[idx]
                idx = (idx + 1) % n
                cnt += 1
                if res < 0:
                    break
            else:
                return i
        return -1



