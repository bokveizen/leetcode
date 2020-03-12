# https://leetcode-cn.com/problems/interleaving-string/
import functools


class Solution:  # simple backtrack w/ lru cache
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3
        if sorted(s1 + s2) != sorted(s3):
            return False
        len1 = len(s1)
        len2 = len(s2)

        @functools.lru_cache(None)  # necessary (or using memo)
        def backtrack(ptr1=0, ptr2=0, ptr3=0):
            # end conditions
            if ptr1 == len1 and ptr2 == len2:
                return True
            if ptr1 == len1:
                return s2[ptr2:] == s3[ptr3:]
            if ptr2 == len2:
                return s1[ptr1:] == s3[ptr3:]
            char1 = s1[ptr1]
            char2 = s2[ptr2]
            char3 = s3[ptr3]
            if char1 == char2:
                if char1 == char3:
                    if backtrack(ptr1 + 1, ptr2, ptr3 + 1) or \
                            backtrack(ptr1, ptr2 + 1, ptr3 + 1):
                        return True
                    return False
                else:
                    return False
            elif char1 == char3:
                return backtrack(ptr1 + 1, ptr2, ptr3 + 1)
            elif char2 == char3:
                return backtrack(ptr1, ptr2 + 1, ptr3 + 1)
            return False

        return backtrack()


class Solution_dp:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3
        if sorted(s1 + s2) != sorted(s3):
            return False
        len1 = len(s1)
        len2 = len(s2)
        dp = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]
        for i in range(len1 + 1):
            for j in range(len2 + 1):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = s2[j - 1] == s3[j - 1] if dp[i][j - 1] else 0
                elif j == 0:
                    dp[i][j] = s1[i - 1] == s3[i - 1] if dp[i - 1][j] else 0
                else:
                    if dp[i - 1][j]:
                        dp[i][j] += s1[i - 1] == s3[i + j - 1]
                    if dp[i][j - 1]:
                        dp[i][j] += s2[j - 1] == s3[i + j - 1]
        return dp[-1][-1] > 0
