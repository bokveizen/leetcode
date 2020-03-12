# https://leetcode-cn.com/problems/greatest-common-divisor-of-strings/
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        candidate_len = math.gcd(len(str1), len(str2))
        if str1 + str2 == str2 + str1:
            return str1[: candidate_len]
        return ''
