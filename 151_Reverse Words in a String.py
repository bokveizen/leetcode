# https://leetcode-cn.com/problems/reverse-words-in-a-string/
class Solution:
    def reverseWords(self, s: str) -> str:
        # return " ".join(s.split()[::-1])
        # 先翻转整个数组
        # 再翻转单个单词
        # 清除多余空格
        n = len(s)
        s = list(s)[::-1]
        i = 0
        while i < n:
            # 找到一个单词首字母
            while i < n and s[i] == " ":
                i += 1
            j = i
            # 找到一个单词末位置
            while j < n and s[j] != " ":
                j += 1
            s[i:j] = s[i:j][::-1]
            i = j

        i = j = 0
        while j < n:
            # 找到一个单词
            while j < n and s[j] == " ":
                j += 1
            # 单词朝前移
            while j < n and s[j] != " ":
                s[i] = s[j]
                i += 1
                j += 1
            # 移动下一个单词
            while j < n and s[j] == " ":
                j += 1
            if j < n:
                s[i] = " "
                i += 1
        return "".join(s[:i])
