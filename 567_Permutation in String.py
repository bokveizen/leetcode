# https://leetcode-cn.com/problems/permutation-in-string/
# sliding window
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n > m:
            return False
        cnt = [0] * 26
        for i in range(n):
            cnt[ord(s1[i]) - 97] += 1
            cnt[ord(s2[i]) - 97] -= 1
        diff = sum(c != 0 for c in cnt)
        if not diff:
            return True
        for i in range(n, m):
            new = ord(s2[i]) - 97
            old = ord(s2[i - n]) - 97
            if new != old:
                if not cnt[new]:
                    diff += 1
                cnt[new] -= 1
                if not cnt[new]:
                    diff -= 1
                if not cnt[old]:
                    diff += 1
                cnt[old] += 1
                if not cnt[old]:
                    diff -= 1
                if not diff:
                    return True
        return False

# double pointers
# class Solution {
# public:
#     bool checkInclusion(string s1, string s2) {
#         int n = s1.length(), m = s2.length();
#         if (n > m) {
#             return false;
#         }
#         vector<int> cnt(26);
#         for (int i = 0; i < n; ++i) {
#             --cnt[s1[i] - 'a'];
#         }
#         int left = 0;
#         for (int right = 0; right < m; ++right) {
#             int x = s2[right] - 'a';
#             ++cnt[x];
#             while (cnt[x] > 0) {
#                 --cnt[s2[left] - 'a'];
#                 ++left;
#             }
#             if (right - left + 1 == n) {
#                 return true;
#             }
#         }
#         return false;
#     }
# };
