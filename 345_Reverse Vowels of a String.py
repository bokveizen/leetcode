# https://leetcode-cn.com/problems/reverse-vowels-of-a-string/submissions/
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = [i for i in s if i in 'aeiouAEIOU']
        index = -1
        res = ''
        for i in range(len(s)):
            if s[i] in 'aeiouAEIOU':
                res += vowels[index]
                index -= 1
            else:
                res += s[i]
        return res
