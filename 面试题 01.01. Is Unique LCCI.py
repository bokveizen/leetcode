# https://leetcode-cn.com/problems/is-unique-lcci/
class Solution:
    def isUnique(self, astr: str) -> bool:
        if not astr:
            return True
        chars = set()
        for char in astr:
            if char in chars:
                return False
            chars.add(char)
        return True
