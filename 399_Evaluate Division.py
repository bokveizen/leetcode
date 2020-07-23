# https://leetcode-cn.com/problems/evaluate-division/
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        val_dicts = [{}]
        index_to_process = list(range(len(equations)))
        remaining_eq_num = len(equations)
        init = True
        while index_to_process:
            for i in index_to_process:
                v1, v2 = equations[i]
                q = values[i]
                if init:
                    val_dicts[-1][v2] = 1.0
                    val_dicts[-1][v1] = q
                    init = False
                    index_to_process.remove(i)
                else:
                    if v1 == v2 or (v1 in val_dicts[-1] and v2 in val_dicts[-1]):
                        index_to_process.remove(i)
                    elif v1 in val_dicts[-1]:
                        val_dicts[-1][v2] = val_dicts[-1][v1] / q
                        index_to_process.remove(i)
                    elif v2 in val_dicts[-1]:
                        val_dicts[-1][v1] = val_dicts[-1][v2] * q
                        index_to_process.remove(i)
            cur_eq_num = len(index_to_process)
            if cur_eq_num == remaining_eq_num:
                init = True
                val_dicts.append({})
            remaining_eq_num = cur_eq_num
        # print(val_dicts)
        res = []
        for q in queries:
            v1, v2 = q
            res_q = -1.
            for vd in val_dicts:
                if (v1 in vd and v2 not in vd) or (v1 not in vd and v2 in vd):
                    break
                elif v1 in vd and v2 in vd:
                    res_q = vd[v1] / vd[v2]
            res.append(res_q)
        return res
