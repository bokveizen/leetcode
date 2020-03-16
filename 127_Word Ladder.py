# https://leetcode-cn.com/problems/word-ladder/
# 方法 1：广度优先搜索
from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        n = len(beginWord)
        helper_dict = defaultdict(list)
        for word in wordList:
            for i in range(n):
                helper_dict[word[:i] + "*" + word[i + 1:]].append(word)

        queue = [(beginWord, 1)]
        visited = [beginWord]
        while queue:
            current_word, level = queue.pop(0)
            for i in range(n):
                key = current_word[:i] + "*" + current_word[i + 1:]
                for word in helper_dict[key]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited.append(word)
                        queue.append((word, level + 1))
                helper_dict[key] = []
        return 0


# 方法 2：双向广度优先搜索
from collections import defaultdict
class Solution:
    def __init__(self):
        self.length = 0
        self.helper_dict = defaultdict(list)

    def queueSearch(self, queue, visited1, visited2):
        current_word, level = queue.pop(0)
        for i in range(self.length):
            key = current_word[:i] + "*" + current_word[i+1:]
            for word in self.helper_dict[key]:
                if word in visited2:
                    return level + visited2[word]
                if word not in visited1:
                    visited1[word] = level + 1
                    queue.append((word, level + 1))
        return 0

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        self.length = len(beginWord)
        for word in wordList:
            for i in range(self.length):
                self.helper_dict[word[:i] + "*" + word[i+1:]].append(word)

        queue1 = [(beginWord, 1)]
        queue2 = [(endWord, 1)]
        visited1 = {beginWord: 1}
        visited2 = {endWord: 1}
        res = 0

        while queue1 and queue2:
            res = self.queueSearch(queue1, visited1, visited2)
            if res:
                return res
            res = self.queueSearch(queue2, visited2, visited1)
            if res:
                return res
        return 0

# timeout
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return False
        res = []
        current_path_len = -1

        def word_diff_one_char(word1, word2):
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    return word1[i + 1:] == word2[i + 1:]

        def backtrack(res_tmp=None):
            if res_tmp is None:
                res_tmp = [beginWord]
            neighbors = [word for word in wordList if word not in res_tmp and word_diff_one_char(word, res_tmp[-1])]
            if not neighbors:
                return
            if endWord in neighbors:
                tmp_len = len(res_tmp) + 1
                nonlocal current_path_len, res
                if current_path_len == -1 or tmp_len < current_path_len:
                    current_path_len = tmp_len
                    res = [res_tmp + [endWord]]
                elif tmp_len == current_path_len:
                    res.append(res_tmp + [endWord])
                else:  # it's a useless path
                    pass
                return
            for neighbor in neighbors:
                backtrack(res_tmp + [neighbor])
            return

        backtrack()
        return res