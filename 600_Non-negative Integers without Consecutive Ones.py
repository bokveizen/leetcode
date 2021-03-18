# https://leetcode-cn.com/problems/non-negative-integers-without-consecutive-ones/
class Solution:
    def findIntegers(self, num: int) -> int:
        dp = [0] * (num + 1)
        res = num + 1
        for i in range(num + 1):
            if i <= num // 2:
                if dp[i] == 0:
                    dp[i << 1] = 0
                    if i << 1 < num:
                        dp[(i << 1) + 1] = 1
                elif dp[i] == 1:
                    dp[i << 1] = 0
                    if i << 1 < num:
                        dp[(i << 1) + 1] = 2
                else:
                    dp[i << 1] = 2
                    if i << 1 < num:
                        dp[(i << 1) + 1] = 2
            if dp[i] == 2:
                res -= 1
        return res

class Solution:
    def findIntegers(self, num: int) -> int:
        f = [0] * 32
        f[0] = 1
        f[1] = 2
        for i in range(2, 32):
            f[i] = f[i - 1] + f[i - 2]
        i, res, pre = 30, 0, 0
        while i >= 0:
            if num & (1 << i):
                res += f[i]
                if pre == 1:
                    res -= 1
                    break
                pre = 1
            else:
                pre = 0
            i -= 1
        return res + 1

# Java
# public class Solution {
#     public int findIntegers(int num) {
#         int[] f = new int[32];
#         f[0] = 1;
#         f[1] = 2;
#         for (int i = 2; i < f.length; i++)
#             f[i] = f[i - 1] + f[i - 2];
#         int i = 30, sum = 0, prev_bit = 0;
#         while (i >= 0) {
#             if ((num & (1 << i)) != 0) {
#                 sum += f[i];
#                 if (prev_bit == 1) {
#                     sum--;
#                     break;
#                 }
#                 prev_bit = 1;
#             } else
#                 prev_bit = 0;
#             i--;
#         }
#         return sum + 1;
#     }
# }



