# https://leetcode-cn.com/problems/3sum-closest/
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        l = len(nums)
        flag = True  # First one
        ans = 0
        for i in range(l - 2):
            for j in range(i + 1, l - 1):
                remain_target = target - nums[i] - nums[j]
                for k in range(j + 1, l):
                    if nums[k] == remain_target:
                        return target
                    if flag:
                        flag = False
                        ans = nums[k] - remain_target  # nums[i] + nums[j] + nums[k] - target
                    elif abs(nums[k] - remain_target) < abs(ans):
                        ans = nums[k] - remain_target
        return target + ans


# Double pointer
class Solution_Double_Printer:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        res = sum(nums[:3])
        for i in range(n - 2):
            L = i + 1
            R = n - 1
            while (L < R):
                cur_res = nums[i] + nums[L] + nums[R]
                if cur_res == target:
                    return target
                if abs(cur_res - target) < abs(res - target):  # a better result
                    res = cur_res
                if cur_res < target:
                    L += 1
                else:
                    R -= 1
        return res
