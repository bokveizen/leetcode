# https://leetcode-cn.com/problems/largest-number/
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def smaller(s, t):
            i = 0
            m = len(s)
            n = len(t)
            while True:
                if s[i % m] == t[i % n]:
                    if i % m == m - 1 and i % n == n - 1:
                        return False
                    i += 1
                    continue
                return s[i % m] < t[i % n]

        def quicksort(xs):
            """Given indexable and slicable iterable, return a sorted list"""
            if xs:  # if given list (or tuple) with one ordered item or more:
                pivot = xs[0]
                # below will be less than:
                below = [i for i in xs[1:] if smaller(i, pivot)]
                # above will be greater than or equal to:
                above = [i for i in xs[1:] if not smaller(i, pivot)]
                return quicksort(above) + [pivot] + quicksort(below)
            else:
                return xs  # empty list

        nums = [str(num) for num in nums]

        res = ''.join(quicksort(nums))
        while len(res) > 1 and res[0] == '0':
            res = res[1:]
        return res
