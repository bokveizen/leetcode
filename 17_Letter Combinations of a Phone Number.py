# https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dict = {'2': 'abc',
                '3': 'def',
                '4': 'ghi',
                '5': 'jkl',
                '6': 'mno',
                '7': 'pqrs',
                '8': 'tuv',
                '9': 'wxyz'}
        res = ['']
        for digit in digits:
            res = [p+s for p in res for s in dict[digit]]
        return res
