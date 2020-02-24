# https://leetcode-cn.com/problems/verifying-an-alien-dictionary/
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        max_word_len = max(len(word) for word in words)

        def word_to_val(word):
            res = 0
            for i in range(max_word_len):
                pos = max_word_len - 1 - i
                if pos < len(word):
                    digit = order.index(word[pos])
                else:
                    digit = 0  # empty char
                res += digit * 27 ** i
            return res

        tmp = -1
        for word in words:
            if word_to_val(word) >= tmp:
                tmp = word_to_val(word)
            else:
                return False
        return True
