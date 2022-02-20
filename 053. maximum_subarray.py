class Solution(object):
    def maxSubArray(self, nums):
        overall_array = [nums[0]]
        current_array = [nums[0]]
        overall_max = nums[0]
        current_max = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > 0:
                current_max += nums[i]
                if current_max > overall_max:
                    overall_max = current_max
