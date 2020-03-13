# https://leetcode-cn.com/problems/word-ladder-ii/
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


# TODO: time optimization

