# https://leetcode-cn.com/problems/minimum-window-substring/
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt_s = Counter(s)
        cnt_t = Counter(t)
        # special cases
        for ch in cnt_t:
            if cnt_s[ch] < cnt_t[ch]:
                return ''
        if len(t) == 1:
            return t

        node_list = [i for i in range(len(s)) if s[i] in t]
        L = 0
        R = len(node_list) - 1
        cnt_current = cnt_s
        # find the largest L for the current R
        while L <= R:
            L_char = s[node_list[L]]
            if cnt_current[L_char] - cnt_t[L_char] >= 1:
                cnt_current[L_char] -= 1
                L += 1
            else:  # can not move L any more
                break
        # try to move R
        while L <= R:
            R_char = s[node_list[R]]
            if cnt_current[R_char] - cnt_t[R_char] >= 1:
                cnt_current[R_char] -= 1
                R -= 1
            else:  # can not move R any more
                break
        res = s[node_list[L]:node_list[R] + 1]
        R_char = s[node_list[R]]
        cnt_current[R_char] -= 1
        R -= 1
        while R >= 0:
            # find the largest L for current R
            while L >= 0:
                L -= 1
                L_char = s[node_list[L]]
                cnt_current[L_char] += 1
                if L_char == R_char:  # a successful makeup
                    break
            if L < 0:  # no L could be found for the current R
                break
            # try to move R
            while L <= R:
                R_char = s[node_list[R]]
                if cnt_current[R_char] - cnt_t[R_char] >= 1:
                    cnt_current[R_char] -= 1
                    R -= 1
                else:  # can not move R any more
                    break
            res_temp = s[node_list[L]:node_list[R] + 1]
            if len(res_temp) < len(res):
                res = res_temp
            R_char = s[node_list[R]]
            cnt_current[R_char] -= 1
            R -= 1
        return res


class Solution_TIMEOUT:
    def minWindow(self, s: str, t: str) -> str:
        def contain(str1, str2):
            for ch in str2:
                if ch not in str1:
                    return False
                ch_pos = str1.index(ch)
                str1 = str1[:ch_pos] + str1[ch_pos + 1:]
            return True

        # special cases
        if not contain(s, t):
            return ''
        if len(t) == 1:
            return t
        # init.
        L = 0
        R = len(s) - 1
        for i in range(len(s)):
            if s[i] in t:
                L = i
                break
        for i in range(len(s)):
            if s[len(s) - 1 - i] in t:
                R = len(s) - 1 - i
                break
        # main loop
        node_list = [i for i in range(L, R + 1) if s[i] in t]
        L = 0
        R = len(node_list) - 1
        while L <= R and contain(s[node_list[L]:node_list[R] + 1], t):
            L += 1
        L -= 1  # the largest L for current R
        while L <= R and contain(s[node_list[L]:node_list[R] + 1], t):
            R -= 1
        R += 1  # the smallest R for current L (which is for the init. R)
        res = s[node_list[L]:node_list[R] + 1]
        R -= 1
        while R >= 0 and contain(s[:node_list[R] + 1], t):
            # find the largest L for current R
            while L >= 0 and not contain(s[node_list[L]:node_list[R] + 1], t):
                L -= 1
            if L < 0:  # no L could be found for the current R
                break
            while L <= R and contain(s[node_list[L]:node_list[R] + 1], t):
                R -= 1
            R += 1  # the smallest R for current L
            res_temp = s[node_list[L]:node_list[R] + 1]
            if len(res_temp) < len(res):
                res = res_temp
            R -= 1
        return res
