# https://leetcode-cn.com/problems/filling-bookcase-shelves/
from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        book_num = len(books)
        dp = [1000 * 1000] * (book_num + 1)
        dp[0] = 0
        for i in range(1, len(dp)):
            last_bookcase = [0, 0]  # [width, height]
            for j in range(i-1, -1, -1):
                last_bookcase[0] += books[j][0]
                if books[j][1] > last_bookcase[1]:
                    last_bookcase[1] = books[j][1]
                if last_bookcase[0] > shelf_width:
                    break
                if dp[j] + last_bookcase[1] < dp[i]:
                    dp[i] = dp[j] + last_bookcase[1]
        return dp[-1]

