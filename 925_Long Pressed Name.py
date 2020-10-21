# https://leetcode-cn.com/problems/long-pressed-name/
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        len_n = len(name)
        len_t = len(typed)
        i = j = 0
        last_char = '-'
        while j < len(typed):
            if len_n > len_t:
                return False
            if i < len(name) and name[i] == typed[j]:  # match one char
                last_char = name[i]
                i += 1
                j += 1
                len_n -= 1
                len_t -= 1
            elif typed[j] == last_char:  # available for long pressing
                j += 1
                len_t -= 1
            else:
                return False
        return i == len(name)
