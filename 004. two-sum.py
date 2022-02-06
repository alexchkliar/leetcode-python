# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You can return the answer in any order.

# O(n) time, O(n) space
class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        for i in range(0, len(nums)):
            if (target - nums[i] in dict):
                return [dict[target - nums[i]], i]
            dict[nums[i]] = i
        return "No matches"


nums1 = [2,7,11,15]
target1 = 9

nums2 = [2,7,11,15]
target2 = 18

nums3 = [2,7,15,15]
target3 = 30

print(Solution().twoSum(nums1, target1))
print(Solution().twoSum(nums2, target2))
print(Solution().twoSum(nums3, target3))
