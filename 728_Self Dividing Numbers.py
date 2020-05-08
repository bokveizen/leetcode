# https://leetcode-cn.com/problems/self-dividing-numbers/
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right + 1):
            if '0' not in str(i):
                for d in str(i):
                    if i % int(d):
                        break
                else:
                    res.append(i)
        return res