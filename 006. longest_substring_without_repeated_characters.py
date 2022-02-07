# Given a string s, find the length of the longest substring without repeating characters.

# to make even more efficient, can track index of first value in latest duplicate value pair
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_count = 0
        iter = 0
        k = len(s)
        for i in range(0, k):
            current_count = 0
            tracker_array = []
            for j in range(i, k):
                if s[j] not in tracker_array:
                    tracker_array += [s[j]]
                    current_count += 1
                    # k += 1
                    if current_count > max_count:
                        max_count = current_count
                else: break
        print(k)
        return max_count


print(Solution().lengthOfLongestSubstring("abcabcbb"))
# print(Solution().lengthOfLongestSubstring("bbbbb"))
# print(Solution().lengthOfLongestSubstring("pwwkew"))
# print(Solution().lengthOfLongestSubstring("au"))
# print(Solution().lengthOfLongestSubstring("aux"))
# print(Solution().lengthOfLongestSubstring(" "))
# print(Solution().lengthOfLongestSubstring(""))
