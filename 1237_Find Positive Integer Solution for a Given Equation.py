# https://leetcode-cn.com/problems/find-positive-integer-solution-for-a-given-equation/
"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):

"""


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        x = 1
        y = z
        f = customfunction.f
        res = []
        while True:
            if x == z + 1 or y == 0:
                return res
            if f(x, y) == z:
                res.append([x, y])
                if x == z or y == 1:
                    return res
                x += 1
                y -= 1
            elif f(x, y) < z:
                x += 1
            else:
                y -= 1
