# O(n), linear because we leep track of min_price_recorded

class Solution(object):
    def maxProfit(self, prices):
        max_gain = 0
        for i in range(0,len(prices)):
            if i == 0: min_price_recorded = prices[0]
            min_price_recorded = min(min_price_recorded, prices[i])
            max_gain = max(max_gain, prices[i] - min_price_recorded)
        return max_gain


print(Solution().maxProfit([7,1,5,3,6,4]))
print(Solution().maxProfit([7,6,4,3,1]))
print(Solution().maxProfit([]))
print(Solution().maxProfit([0]))
print(Solution().maxProfit([1,1,1]))
print(Solution().maxProfit([5]))
print(Solution().maxProfit([4,2,3,4,5]))
