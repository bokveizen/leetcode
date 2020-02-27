# https://leetcode-cn.com/problems/merge-intervals/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n <= 1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        current = 0
        # res = [intervals[0]]
        while current < len(intervals) - 1:
            if intervals[current + 1][0] <= intervals[current][1]:  # can merge
                merged = [intervals[current][0], max(intervals[current][1], intervals[current + 1][1])]
                intervals.pop(current)
                intervals[current] = merged
            else:  # can not merge
                current += 1
        return intervals
