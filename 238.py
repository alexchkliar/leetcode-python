# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

class Solution(object):
    def productExceptSelf(self, nums):
        output = []
        total = 1
        for i in range(0, len(nums)):
            total *= nums[i]

        for i in range(0, len(nums)):
            output[i] = total - (nums[i] - 1)

        return output

print(Solution().productExceptSelf([1,2,3,4]))
