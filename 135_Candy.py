# https://leetcode-cn.com/problems/candy/
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n <= 1:
            return n
        if n == 2:
            return 3 if ratings[0] != ratings[1] else 2
        left = [1] * n
        right = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
        res = left[-1]
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1
            res += max(left[i], right[i])
        return res


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n <= 1:
            return n
        if n == 2:
            return 3 if ratings[0] != ratings[1] else 2
        tmp = [1] * n

        def check():
            for i in range(n):
                if i == 0:
                    if ratings[0] > ratings[1] and tmp[0] <= tmp[1]:
                        tmp[0] = tmp[1] + 1
                        return False
                elif i == n - 1:
                    if ratings[n - 1] > ratings[n - 2] and tmp[n - 1] <= tmp[n - 2]:
                        tmp[n - 1] = tmp[n - 2] + 1
                        return False
                else:
                    if (ratings[i] > ratings[i + 1] and tmp[i] <= tmp[i + 1]) and \
                            (ratings[i] > ratings[i - 1] and tmp[i] <= tmp[i - 1]):
                        tmp[i] = max(tmp[i - 1], tmp[i + 1]) + 1
                        return False
                    elif ratings[i] > ratings[i + 1] and tmp[i] <= tmp[i + 1]:
                        tmp[i] = tmp[i + 1] + 1
                        return False
                    elif ratings[i] > ratings[i - 1] and tmp[i] <= tmp[i - 1]:
                        tmp[i] = tmp[i - 1] + 1
                        return False
            return True

        while not check():
            pass
        return sum(tmp)
