# https://leetcode-cn.com/problems/insert-interval/
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        if n == 0:
            return [newInterval]
        # intervals.sort(key=lambda x: x[0])
        current = 0
        if newInterval[0] <= intervals[0][0]:
            intervals = [newInterval] + intervals
        elif newInterval[0] >= intervals[-1][0]:
            intervals = intervals + [newInterval]
        else:
            for i in range(n - 1):
                if intervals[i][0] <= newInterval[0] <= intervals[i + 1][0]:
                    intervals.insert(i + 1, newInterval)
                    break
        while current < len(intervals) - 1:
            if intervals[current + 1][0] <= intervals[current][1]:  # can merge
                merged = [intervals[current][0], max(intervals[current][1], intervals[current + 1][1])]
                intervals.pop(current)
                intervals[current] = merged
            else:  # can not merge
                current += 1
        return intervals
