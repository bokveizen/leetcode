# https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if any(c in '0123456789' for c in token):
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if token == '+':
                    res = num1 + num2
                elif token == '-':
                    res = num1 - num2
                elif token == '*':
                    res = num1 * num2
                else:
                    res = abs(num1) // abs(num2)
                    if (num1 < 0) ^ (num2 < 0):
                        res = -res
                stack.append(res)
        return stack.pop()
