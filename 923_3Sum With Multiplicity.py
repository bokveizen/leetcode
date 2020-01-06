# https://leetcode-cn.com/problems/3sum-with-multiplicity/
from collections import Counter
from typing import List


class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        c = Counter(A)
        if max(A) * 3 < target:
            return 0
        res = 0
        largest_num_lower_bound = (target - 1) // 3
        for i in range(min(target, max(A)), largest_num_lower_bound, -1):
            if i not in c:
                continue
            smallest_num_upper_bound = (target - i + 2) // 2
            for j in range(max(0, target - 2 * i), smallest_num_upper_bound):
                m = target - i - j
                if j not in c or m not in c:
                    continue
                # assert i >= m >= j, '{} {} {} {}'.format(i, m, j, target)
                if i != m and i != j and m != j:
                    res += c[i] * c[m] * c[j]
                    res %= 10 ** 9 + 7
                elif i == m == j:
                    res += c[i] * (c[i] - 1) * (c[i] - 2) // 6
                    res %= 10 ** 9 + 7
                elif i == m:
                    res += (c[m] * (c[m] - 1) // 2) * c[j]
                    res %= 10 ** 9 + 7
                else:  # j == m
                    res += (c[m] * (c[m] - 1) // 2) * c[i]
                    res %= 10 ** 9 + 7
        return res
