# https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        word_len = len(words[0])
        word_num = len(words)
        if len(s) < word_len * word_num:
            return []
        res = []
        cnt = Counter(words)
        for i in range(len(s) - word_len * word_num + 1):
            cur = s[i:i + word_len * word_num]
            cur_words = [cur[s * word_len:(s + 1) * word_len] for s in range(word_num)]
            if Counter(cur_words) == cnt:
                res.append(i)
        return res
