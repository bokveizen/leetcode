# https://leetcode-cn.com/problems/escape-the-ghosts/

class Solution:
    def dist(self, p1, p2):
        return sum([abs(p1[i] - p2[i]) for i in range(len(p1))])

    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        return min(self.dist(target, ghost) for ghost in ghosts) > self.dist(target, [0, 0])

# class Solution:
#     def dist(self, p1, p2):
#         return sum([abs(p1[i] - p2[i]) for i in range(len(p1))])
#
#     def sign(self, num):
#         if num > 0:
#             return 1
#         if num < 0:
#             return -1
#         return 0
#
#     def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
#         start_pos = current_pos = [0, 0]
#         if [0, 0] in ghosts:
#             return False
#         elif target == [0, 0]:
#             return True
#         while True:
#             if current_pos == target:
#                 return True
#             if target[0] == 0:
#                 next_pos_list = [[0, current_pos[1] + self.sign(target[1])]]
#             elif target[1] == 0:
#                 next_pos_list = [[current_pos[0] + self.sign(target[0]), 0]]
#             else:
#                 next_pos_list = [[current_pos[0] + self.sign(target[0]), current_pos[1]],
#                                  [current_pos[0], current_pos[1] + self.sign(target[1])]]
#             min_dist_list = []
#             for next_pos in next_pos_list:
#                 if self.dist(next_pos, target) > self.dist(current_pos, target):
#                     min_dist_list.append(-1)
#                     continue
#                 min_dist = min([self.dist(next_pos, ghost) - self.dist(next_pos, start_pos) for ghost in ghosts])
#                 min_dist_list.append(min_dist)
#             if max(min_dist_list) <= 0:
#                 return False
#             else:
#                 current_pos = next_pos_list[min_dist_list.index(max(min_dist_list))]
