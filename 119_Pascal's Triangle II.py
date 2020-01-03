# https://leetcode-cn.com/problems/pascals-triangle-ii/
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        index = 2
        row = [1, 1]

        def list_add(list1, list2):
            return [a + b for a, b in zip(list1, list2)]

        while True:
            new_row = [row[0]] + list_add(row[:-1], row[1:]) + [row[-1]]
            if index == rowIndex:
                return new_row
            index += 1
            row = new_row
