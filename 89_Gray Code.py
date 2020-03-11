# https://leetcode-cn.com/problems/gray-code/
class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        res = [0]
        for i in range(1, n + 1):
            res += [2 ** (i - 1) + num for num in res[::-1]]
        return res
