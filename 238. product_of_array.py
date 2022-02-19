# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

class Solution(object):
    def productExceptSelf(self, nums):
        prefix_products = [None] * len(nums)
        suffix_products = [None] * len(nums)
        output = [None] * len(nums)
        for i in range(0, len(nums)):
            if i == 0:
                prefix_products[0] = suffix_products[-1] = 1
            else:
                prefix_products[i] = nums[i - 1] * prefix_products[i - 1]
                suffix_products[-i - 1] = nums[-i] * suffix_products[-i]
        for i in range(0,len(nums)):
            output[i] = prefix_products[i] * suffix_products[i]
        return output

print(Solution().productExceptSelf([1,2,3,4,5]))
