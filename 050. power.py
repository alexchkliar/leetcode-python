import math

class Solution(object):
    def myPow(self, x, n):
        # print(n)
        if n == 0:
            return 1
        if n == 1:
            return x
        if n % 2 == 0:
            return Solution().myPow(x, math.floor(n/2)) ** 2
        return x * Solution().myPow(x, math.floor(n/2)) ** 2


print(Solution().myPow(2,4))
print(Solution().myPow(2,5))
print(Solution().myPow(2,1))
