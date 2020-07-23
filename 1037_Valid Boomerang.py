# https://leetcode-cn.com/problems/valid-boomerang/
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        # if points[0] == points[1] or points[0] == points[2] or points[1] == points[2]:
        #     return False
        # if points[0][0] == points[1][0] == points[2][0] or points[0][1] == points[1][1] == points[2][1]:
        #     return False
        if (points[1][0] - points[0][0]) * (points[2][1] - points[1][1]) == (points[1][1] - points[0][1]) * (points[2][0] - points[1][0]):
            return False
        return True
