# https://leetcode-cn.com/problems/split-array-into-consecutive-subsequences/
from collections import *
import heapq


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        lens = dict()
        for num in nums:
            if num - 1 in lens:
                min_len = heapq.heappop(lens[num - 1])
                if not lens[num - 1]:
                    del lens[num - 1]
                if num in lens:
                    heapq.heappush(lens[num], min_len + 1)
                else:
                    lens[num] = [min_len + 1]
            else:
                if num in lens:
                    heapq.heappush(lens[num], 1)
                else:
                    lens[num] = [1]
        for v in lens.values():
            if v[0] < 3:
                return False
        return True


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        cnt = Counter(nums)
        seq = defaultdict(int)
        for num in nums:
            if cnt[num]:
                if seq[num - 1]:
                    cnt[num] -= 1
                    seq[num - 1] -= 1
                    seq[num] += 1
                else:
                    cnt[num] -= 1
                    if cnt[num + 1]:
                        cnt[num + 1] -= 1
                    else:
                        return False
                    if cnt[num + 2]:
                        cnt[num + 2] -= 1
                    else:
                        return False
                    seq[num + 2] += 1
        return True
