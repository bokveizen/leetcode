# https://leetcode-cn.com/problems/number-of-students-doing-homework-at-a-given-time/
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        res = 0
        n = len(startTime)
        for i in range(n):
            if startTime[i] <= queryTime <= endTime[i]:
                res += 1
        return res
