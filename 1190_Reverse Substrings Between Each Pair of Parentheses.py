# https://leetcode-cn.com/problems/reverse-substrings-between-each-pair-of-parentheses/
class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        if n == 2:
            return '' if s == '()' else s
        stack = []
        for ch in s:
            if ch == ')':
                tmp = []
                while True:
                    t = stack.pop()
                    if t == '(':
                        stack += tmp
                        break
                    else:
                        tmp.append(t)
            else:
                stack.append(ch)
        return ''.join(stack)
