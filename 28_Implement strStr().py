# https://leetcode-cn.com/problems/implement-strstr/
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1
        for i in range(len(haystack) - len(needle) + 1):
            flag = True
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    flag = False
                    break
            if flag:
                return i
        return -1
