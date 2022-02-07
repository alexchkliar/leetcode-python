class Solution(object):
    def isPalindrome(self, x):
        x_as_string_array = list(str(x))
        for i in range(0, len(x_as_string_array)//2 + 1):
            if x_as_string_array[i] != x_as_string_array[len(x_as_string_array) - i - 1]:
                return False
        return True

print(Solution().isPalindrome(121))
print(Solution().isPalindrome(555))
print(Solution().isPalindrome(4444))
print(Solution().isPalindrome(12321))
print(Solution().isPalindrome(0))
print(Solution().isPalindrome(1))
print(Solution().isPalindrome(-121))
print(Solution().isPalindrome(10))
