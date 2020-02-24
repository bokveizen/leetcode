# https://leetcode-cn.com/problems/max-consecutive-ones-iii/
from typing import List


class Solution_TIMEOUT:
    def longestOnes(self, A: List[int], K: int) -> int:
        if sum(A) + K >= len(A):
            return len(A)
        current_term = 1
        current_counting = 0
        counting_res = []
        for i in A:
            if i == current_term:
                current_counting += 1
            else:
                counting_res.append(current_counting)
                current_term = 1 - current_term
                current_counting = 1
        counting_res.append(current_counting)
        if K == 0:
            return max(counting_res[::2])
        res = 0

        def max_turning_range(start_pos, total):
            zero_list = counting_res[1::2]
            start_pos = start_pos // 2
            end_pos = start_pos
            remaining = total
            while True:
                if end_pos >= len(zero_list):
                    return -3, remaining
                elif remaining < zero_list[end_pos]:
                    return 2 * end_pos - 1, remaining
                else:
                    remaining -= zero_list[end_pos]
                    end_pos += 1

        for i in range(1, len(counting_res), 2):
            if counting_res[i] > K:
                res = max(res, K + max(counting_res[i - 1], counting_res[i + 1]))
            else:
                end_point, remaining_k = max_turning_range(i, K)
                if end_point < 0:
                    new_res = sum(counting_res[i - 1:]) + remaining_k
                    res = max(res, new_res)
                    break
                else:
                    new_res = sum(counting_res[i - 1:end_point + 2]) + remaining_k
                    res = max(res, new_res)
        return res


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        if sum(A) + K >= len(A):  # all 1 is possible
            return len(A)
        if K == 0:  # Max Consecutive Ones
            res = cnt = 0
            for num in A:
                if num == 0:
                    res = max(res, cnt)
                    cnt = 0
                else:
                    cnt += 1
            return max(res, cnt)
        left = right = res = cnt = 0
        while right < len(A):
            K -= 1 - A[right]  # consume
            while K < 0:
                K += 1 - A[left]
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res
