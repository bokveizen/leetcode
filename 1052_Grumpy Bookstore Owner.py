# https://leetcode-cn.com/problems/grumpy-bookstore-owner/
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n = len(customers)
        customers_base_sum = 0
        customers_add = []
        for i in range(n):
            base, add = (0, customers[i]) if grumpy[i] else (customers[i], 0)
            customers_base_sum += base
            customers_add.append(add)
        add_max = sum(customers_add[:X])
        last = add_max
        for i in range(X, n):
            last += customers_add[i] - customers_add[i - X]
            add_max = max(add_max, last)
        return add_max + customers_base_sum
