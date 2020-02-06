# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class SolutionBisection:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        if nums[0] > target or nums[-1] < target:
            return [-1, -1]
        left = res_l = 0
        right = res_r = len(nums) - 1

        def find_board(start, end, right_board):
            if right_board:
                if nums[end] == target:  # whole interval = target
                    return end
                if nums[start] != target:  # whole interval != target
                    return start - 1
                # partly = target (start = tgt, end != tgt)
                while end >= start + 2:
                    mid = (start + end) // 2
                    if nums[mid] == target:
                        if nums[mid + 1] != target:
                            return mid
                        else:
                            start = mid + 1
                    else:  # mid != tgt
                        if nums[mid - 1] == target:
                            return mid - 1
                        else:
                            end = mid - 1
                return start
            else:  # left board
                if nums[start] == target:
                    return start
                if nums[end] != target:
                    return end + 1
                # partly = target (start != tgt, end = tgt)
                while end >= start + 2:
                    mid = (start + end) // 2
                    if nums[mid] == target:
                        if nums[mid - 1] != target:
                            return mid
                        else:
                            end = mid - 1
                    else:  # mid != tgt
                        if nums[mid + 1] == target:
                            return mid + 1
                        else:
                            start = mid + 1
                return end

        while right >= left + 2:  # [left, right] interval >= 3
            mid = (left + right) // 2
            if nums[mid] == target:
                # if nums[left] == target:
                #     res_l = left
                # if nums[right] == target:
                #     res_r = right
                res_l = find_board(left, mid - 1, False)
                res_r = find_board(mid + 1, right, True)
                return [res_l, res_r]
            elif nums[mid] < target:
                left = mid + 1
            else:  # mid > target
                right = mid - 1
        # interval <= 2
        if nums[left] != target and nums[right] != target:
            return [-1, -1]
        if nums[left] != target:
            return [right, right]
        if nums[right] != target:
            return [left, left]
        return [left, right]


class SolutionLinearSearch:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        found = False
        res = [-1, -1]
        for i in range(len(nums)):
            if found and nums[i] != target:
                return res
            if nums[i] == target:
                if not found:
                    found = True
                    res[0] = i
                    res[1] = i
                    if nums[-1] == target:
                        return [i, len(nums) - 1]
                else:
                    res[1] = i
        return res
