# https://leetcode-cn.com/problems/group-anagrams/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        if n == 0:
            return []
        if n == 1:
            return [strs]
        res = []
        for str in strs:
            if not res:
                res.append([str])
            else:
                found = False
                for group in res:
                    if len(str) != len(group[0]):
                        continue
                    match_case = group[0]
                    match = True
                    for char in str:
                        if char not in match_case:
                            match = False
                            break
                        else:
                            char_pos = match_case.index(char)
                            match_case = match_case[:char_pos] + match_case[char_pos + 1:]
                    if match:
                        group.append(str)
                        found = True
                        break
                if not found:
                    res.append([str])
        return res

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        for s in strs:
            res[tuple(sorted(s))].append(s)
        return list(res.values())
