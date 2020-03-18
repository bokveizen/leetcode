# https://leetcode-cn.com/problems/find-words-that-can-be-formed-by-characters/
from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        if not words:
            return 0
        chars_cnt = Counter(chars)
        res = 0
        for word in words:
            word_cnt = Counter(word)
            for c in word_cnt:
                if chars_cnt[c] < word_cnt[c]:
                    break
            # 在Python中的while或者for循环之后还可以有else子句，作用是for循环中if条件一直不满足，则最后就执行else语句
            else:
                res += len(word)
        return res
