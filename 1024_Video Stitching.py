# https://leetcode-cn.com/problems/video-stitching/
class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        if T == 0:
            return 0
        clips.sort()
        dp = [-1] * (T + 1)
        dp[0] = 0
        for t_s, t_e in clips:
            if t_s > T:
                return dp[-1]
            if dp[t_s] == -1:
                return -1
            for i in range(t_s + 1, min(t_e + 1, T + 1)):
                if dp[i] == -1 or dp[t_s] + 1 < dp[i]:
                    dp[i] = dp[t_s] + 1
        return dp[-1]
