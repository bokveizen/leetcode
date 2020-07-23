# https://leetcode-cn.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        product = 1
        while n:
            sum += n % 10
            product *= n % 10
            n //= 10
        return product - sum
