# https://leetcode-cn.com/problems/search-a-2d-matrix/
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0] or not matrix[0][0] <= target <= matrix[-1][-1]:
            return False
        m = len(matrix)
        n = len(matrix[0])

        def search_1d(row, left, right):
            if row[left] == target or row[right] == target:
                return True
            if not row[left] < target < row[right]:
                return False
            while left + 2 <= right:
                mid = (left + right) // 2
                if row[mid] == target:
                    return True
                if row[mid] < target:
                    left = mid
                else:
                    right = mid
            return False

        if m == 1:
            return search_1d(matrix[0], 0, n - 1)
        if n == 1:
            return search_1d([row[0] for row in matrix], 0, m - 1)
        up = 0
        down = m - 1
        decided = -1
        if matrix[up][0] == target or matrix[down][0] == target:
            return True
        if target > matrix[down][0]:
            return search_1d(matrix[down], 1, n - 1)
        # matrix[up][0] < target < matrix[down][0]
        while up + 2 <= down:
            mid = (up + down) // 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] < target:
                up = mid
            else:
                down = mid
        return search_1d(matrix[up], 1, n - 1)
