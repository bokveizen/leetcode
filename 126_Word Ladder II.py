# https://leetcode-cn.com/problems/word-ladder-ii/
from collections import defaultdict
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        n = len(beginWord)
        helper_dict = defaultdict(list)
        for word in wordList:
            for i in range(n):
                helper_dict[word[:i] + "*" + word[i + 1:]].append(word)
        queue = [(beginWord, 1)]
        visited = {beginWord: (None, 1)}
        end_level = None
        while queue:
            current_word, level = queue.pop(0)
            if level == end_level:
                break
            for i in range(n):
                key = current_word[:i] + "*" + current_word[i + 1:]
                for word in helper_dict[key]:
                    if word == endWord:
                        if not end_level:
                            end_level = level + 1
                    if word not in visited:
                        visited[word] = ([current_word], level + 1)
                        queue.append((word, level + 1))
                    else:  # word already in visited
                        if level + 1 == visited[word][1]:
                            visited[word][0].append(current_word)
        if not end_level:
            return []
        # print(visited)
        res = [[endWord]]
        for i in range(end_level - 1):
            tmp = []
            for cur in res:
                first = cur[0]
                prev_list = visited[first][0]
                for prev in prev_list:
                    tmp.append([prev] + cur)
                res = tmp
        return res





# timeout
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return False
        res = []
        current_path_len = -1

        def word_diff(word1, word2):
            return sum(a != b for a, b in zip(word1, word2))

        def backtrack(res_tmp=None):
            if res_tmp is None:
                res_tmp = [beginWord]
            neighbors = [word for word in wordList if word not in res_tmp and word_diff(word, res_tmp[-1]) == 1]
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
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        def word_diff(word1, word2):
            return sum(a != b for a, b in zip(word1, word2))

        dist = dict()
        for word in wordList:
            dist[word] = -1
        dist[beginWord] = 0
        visited = [beginWord]
        flag = True
        while flag:
            flag = False
            visited_len = len(visited)
            for cur in wordList:
                if cur not in visited:
                    for i in range(visited_len):
                        if word_diff(visited[i], cur) == 1:
                            if not flag:
                                flag = True
                            if dist[cur] == -1:
                                visited.append(cur)
                                dist[cur] = dist[visited[i]] + 1
                            else:
                                dist[cur] = min(dist[cur], dist[visited[i]] + 1)

        if dist[endWord] == -1:
            return []
        res = [[beginWord]]
        dist_to_end = dist[endWord]
        for i in range(dist_to_end):
            cur_dist = i + 1
            tmp = []
            for cur_res in res:
                cur_word = cur_res[-1]
                if cur_dist < dist_to_end:
                    for word in wordList:
                        if dist[word] == cur_dist and word_diff(word, cur_word) == 1:
                            tmp.append(cur_res + [word])
                else:
                    if word_diff(endWord, cur_word) == 1:
                        tmp.append(cur_res + [endWord])
            if cur_dist < dist_to_end:
                res = tmp
            else:
                return tmp
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        def word_diff(word1, word2):
            return sum(a != b for a, b in zip(word1, word2))

        dist = dict()
        for word in wordList:
            dist[word] = (-1, [])
        dist[beginWord] = (0, [])
        visited = [beginWord]
        flag = True
        while flag:
            flag = False
            visited_len = len(visited)
            for cur in wordList:
                if cur not in visited:
                    for i in range(visited_len):
                        if word_diff(visited[i], cur) == 1:
                            if not flag:
                                flag = True
                            if dist[cur][0] == -1:
                                visited.append(cur)
                                dist[cur] = (dist[visited[i]][0] + 1, [visited[i]])
                            elif dist[visited[i]][0] + 1 < dist[cur][0]:
                                dist[cur] = (dist[visited[i]][0] + 1, [visited[i]])
                            elif dist[visited[i]][0] + 1 == dist[cur][0]:
                                dist[cur][1].append(visited[i])
                            else:  # use less
                                pass
        if dist[endWord][0] == -1:
            return []

        res = [[endWord]]
        for _ in range(dist[endWord][0]):
            tmp = []
            for cur_res in res:
                for pre_word in dist[cur_res[0]][1]:
                    tmp.append([pre_word] + cur_res)
            res = tmp
        return res




