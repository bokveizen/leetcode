# https://leetcode-cn.com/problems/restore-ip-addresses/
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        if n > 12 or n < 4:
            return []

        res = []
        seg_list = []

        def legal_num(num_s):
            # official solution
            # return int(num_s) <= 255 if num_s[0] != '0' else len(num_s) == 1
            if len(num_s) > 3 or not num_s:
                return False
            if len(num_s) == 3:
                if num_s[0] == '1':
                    return True
                if num_s[0] == '2':
                    return int(num_s[1:]) <= 55
                return False
            if len(num_s) == 2:
                return num_s[0] != '0'
            return True

        if n == 12:
            if all(legal_num(num_s) for num_s in (s[3 * i:3 * (i + 1)] for i in range(4))):
                return ['.'.join((s[3 * i:3 * (i + 1)] for i in range(4)))]
            return []
        if n == 4:
            return ['.'.join(s)]

        def backtrack(pre_pos=-1, remaining_dots=3):
            for cur_pos in range(max(pre_pos + 1, n - 3 * remaining_dots - 1), min(pre_pos + 4, n - remaining_dots)):
                seg = s[pre_pos + 1:cur_pos + 1]
                if legal_num(seg):
                    seg_list.append(seg)
                    if remaining_dots == 1:  # it's the last dot
                        final_seg = s[cur_pos + 1:n]
                        if legal_num(final_seg):
                            seg_list.append(final_seg)
                            res.append('.'.join(seg_list))
                            seg_list.pop()
                    else:
                        backtrack(cur_pos, remaining_dots - 1)
                    seg_list.pop()

        backtrack()
        return res
