# https://leetcode-cn.com/problems/multiply-strings/
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1)):
            pos1 = -1 - i
            digit1 = int(num1[pos1])
            for j in range(len(num2)):
                pos2 = -1 - j
                digit2 = int(num2[pos2])
                part_product = res[pos1 + pos2 + 1] + digit1 * digit2
                res[pos1 + pos2 + 1] = part_product % 10
                res[pos1 + pos2] = part_product // 10
        res_str = ''
        for digit in res:
            if digit == 0 and not res_str:
                continue
            else:
                res_str += str(digit)
        return res_str
