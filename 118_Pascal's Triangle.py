# https://leetcode-cn.com/problems/pascals-triangle/
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        def list_add(list1, list2):
            return [a + b for a, b in zip(list1, list2)]
        res = [[1]]
        for _ in range(numRows-1):
            row = res[-1]
            res += [[row[0]] + list_add(row[:-1], row[1:]) + [row[-1]]]
        return res
