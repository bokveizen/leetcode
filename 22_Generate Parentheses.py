# https://leetcode-cn.com/problems/generate-parentheses/
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return ['']
        res = ['({}){}'.format(left, right) for c in range(n)
               for left in self.generateParenthesis(c) for right in self.generateParenthesis(n - 1 - c)]
        return res
