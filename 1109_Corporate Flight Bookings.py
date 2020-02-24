# https://leetcode-cn.com/problems/corporate-flight-bookings/

# TIME OUT
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * n
        for booking in bookings:
            for i in range(booking[0], booking[1] + 1):
                res[i - 1] += booking[2]
        return res


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * n
        for booking in bookings:
            res[booking[0] - 1] += booking[2]
            if booking[1] < len(res):
                res[booking[1]] -= booking[2]
        for i in range(1, len(res)):
            res[i] += res[i - 1]
        return res
