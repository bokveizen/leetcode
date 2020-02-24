# https://leetcode-cn.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        res = ''
        for i in range(min(len(str) for str in strs)):
            for str in strs:
                if str[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res