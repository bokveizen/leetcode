# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        res = 1
        left = right = 0
        while right < len(s) - 1:
            current_str = s[left:right + 1]
            if s[right + 1] not in current_str:
                right += 1
            else:
                res = max(res, right - left + 1)
                repeat_pos = current_str.index(s[right + 1])
                left += repeat_pos + 1
                right += 1
        res = max(res, right - left + 1)
        return res
