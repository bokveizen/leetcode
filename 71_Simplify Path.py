# https://leetcode-cn.com/problems/simplify-path/
class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path or path == '/':
            return '/'
        # del first /
        while path and path[0] == '/':
            path = path[1:]
        if not path:
            return '/'
        # del / at the end
        while path and path[-1] == '/':
            path = path[:-1]
        if not path:
            return '/'
        # del duplicated /
        while '//' in path:
            pos = path.index('//')
            path = path[:pos] + path[pos + 1:]
        path_list = path.split('/')
        history = []
        for i in path_list:
            if i == '..':
                if history:
                    history.pop()
            elif i == '.':
                continue
            else:
                history.append(i)
        res = ''
        for i in history:
            res += '/' + i
        return res if res else '/'


