# https://leetcode-cn.com/problems/number-of-valid-words-for-each-puzzle/
from collections import defaultdict


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        words_cnt = dict()
        for word in words:
            bitmap = 0
            for ch in word:
                bitmap |= (1 << (ord(ch) - ord('a')))
            if bitmap not in words_cnt:
                words_cnt[bitmap] = 1
            else:
                words_cnt[bitmap] += 1
        res = []
        for puzzle in puzzles:
            cnt = bitmap = 0
            for ch in puzzle:
                bitmap |= (1 << (ord(ch) - ord('a')))
            if bitmap in words_cnt:
                cnt += words_cnt[bitmap]
            tmp = bitmap
            while tmp:
                tmp = (tmp - 1) & bitmap
                if (1 << ord(puzzle[0]) - ord('a')) & tmp and tmp in words_cnt:
                    cnt += words_cnt[tmp]
            res.append(cnt)
        return res

# class Solution:
#     def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
#         freq = collections.Counter()
#         for word in words:
#             mask = 0
#             for c in word:
#                 mask |= 1 << (ord(c) - ord('a'))
#             freq[mask] += 1
#         res = []
#         for puzzle in puzzles:
#             total = 0
#             for perm in self.subsets(puzzle[1:]):
#                 mask = 1 << (ord(puzzle[0]) - ord('a'))
#                 for c in perm:
#                     mask |= 1 << (ord(c) - ord('a'))
#                 total += freq[mask]
#             res.append(total)
#         return res
#
#     def subsets(self, words: List[int]) -> List[List[int]]:
#         res = [""]
#         for i in words:
#             res = res + [i + word for word in res]
#         return res

# class Solution {
# public:
#     vector<int> findNumOfValidWords(vector<string>& words, vector<string>& puzzles) {
#         unordered_map<int, int> count;
#         for (string &word: words) {
#             int mask = 0;
#             for (char ch : word)
#                 mask |= (1 << (ch - 'a'));
#             ++count[mask];
#         }
#
#         int n = puzzles.size();
#         vector<int> ret(n, 0);
#         for (int i = 0; i < n; i++) {
#             string &puzzle = puzzles[i];
#             int k = 0;
#             for (char ch: puzzle) {
#                 k |= (1 << (ch - 'a'));
#             }
#
#             int sub = k;
#             do {
#                 sub = (sub - 1) & k;
#                 if ((1 << (puzzle[0] - 'a')) & sub)
#                     ret[i] += count[sub];
#             } while (sub != k);
#         }
#         return ret;
#     }
# };
