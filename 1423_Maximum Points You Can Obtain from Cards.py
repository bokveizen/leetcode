# https://leetcode-cn.com/problems/maximum-points-you-can-obtain-from-cards/
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        res = sum(cardPoints[:k])
        cur = res
        for i in range(k):
            cur += cardPoints[-1 - i] - cardPoints[k - 1 - i]
            if cur > res:
                res = cur
        return res
