# https://leetcode-cn.com/problems/decoded-string-at-index/
class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        # first solution (TIMEOUT)
        # cur_len = 0
        # ptr = {}
        #
        # def find(index):
        #     while True:
        #         if isinstance(ptr[index], str):
        #             return ptr[index]
        #         else:  # number
        #             index = ptr[index]
        #
        # for s in S:
        #     if s.isdigit():
        #         num_s = int(s)
        #         if cur_len * num_s >= K:
        #             return find((K - 1) % cur_len)
        #         for i in range(1, num_s):
        #             for j in range(cur_len):
        #                 ptr[cur_len * i + j] = j
        #         cur_len *= num_s
        #     else:  # letter
        #         ptr[cur_len] = s
        #         cur_len += 1
        #         if cur_len >= K:
        #             return s

        # Sol 2 (still TIMEOUT)
        # now_letter = True
        # cur_str = ''
        # cur_times = 1
        # for s in S:
        #     if now_letter:
        #         if s.isdigit():
        #             now_letter = False
        #             cur_times *= int(s)
        #             if len(cur_str) * cur_times >= K:
        #                 return cur_str[(K - 1) % len(cur_str)]
        #         else:  # continue input char
        #             cur_str += s
        #             if len(cur_str) == K:  # arrive index K by inputting a single char
        #                 return s
        #     else:  # now digit
        #         if s.isdigit():  # continue multiply
        #             cur_times *= int(s)
        #             if len(cur_str) * cur_times >= K:
        #                 return cur_str[(K - 1) % len(cur_str)]
        #         else:  # start to input a new str
        #             cur_str *= cur_times
        #             now_letter = True
        #             cur_times = 1
        #             cur_str += s
        #             if len(cur_str) == K:  # arrive index K by inputting a single char
        #                 return s

        size = 0
        for c in S:
            if c.isdigit():
                size *= int(c)
            else:
                size += 1

        for c in reversed(S):
            K %= size
            if K == 0 and c.isalpha():
                return c
            if c.isdigit():
                size /= int(c)
            else:
                size -= 1

