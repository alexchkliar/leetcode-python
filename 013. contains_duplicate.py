class Solution(object):
    def containsDuplicate(self, nums):
        dict = {}
        for i in range(0,len(nums)):
            if nums[i] in dict:
                return True
            else:
                dict[nums[i]] = 1
        return False


print(Solution().containsDuplicate([1,2,3,4,5]))
print(Solution().containsDuplicate([1,1,3,3,5]))
print(Solution().containsDuplicate([0]))
print(Solution().containsDuplicate([0, 0]))
print(Solution().containsDuplicate([]))
print(Solution().containsDuplicate([5,2,3,4,5]))
