# https://leetcode-cn.com/problems/word-pattern/
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        word_list = str.split(' ')
        if len(pattern) != len(word_list):
            return False
        dct = {}
        for i in range(len(pattern)):
            if pattern[i] not in dct:
                dct[pattern[i]] = word_list[i]
            elif dct[pattern[i]] != word_list[i]:
                return False
        if len(set([dct[i] for i in dct])) == len(dct):
            return True
