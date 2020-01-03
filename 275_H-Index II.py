# https://leetcode-cn.com/problems/h-index-ii/
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations or citations[-1] == 0:
            return 0
        if len(citations) == 1:
            return 1
        # at least 1
        left = - len(citations)
        right = - 1
        while True:
            if right - left == 1:
                if citations[left] >= -left:
                    return -left
                return -right
            current = (left + right) // 2
            if citations[current] == -current:
                return -current
            elif citations[current] > -current:
                right = current
            else:
                left = current
