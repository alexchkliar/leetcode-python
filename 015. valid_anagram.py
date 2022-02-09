class Solution(object):
    def isAnagram(self, s, t):
        dict = {}
        if len(s) != len(t) or len(s) == 0:
            return False
        for i in range(0, len(s)):
            if s[i] in dict:
                dict[s[i]] += 1
            else:
                dict[s[i]] = 1

        for i in range(0, len(t)):
            if t[i] in dict:
                dict[t[i]] -= 1

        for i in range(0, len(s)):
            if dict[s[i]] != 0:
                return False

        return True

        # if len(s) != len(t) or len(s) == 0:
        #     return False
        # for i in range(0, len(s)):
        #     if s[i] != t[len(t) - i - 1]:
        #         return False
        # return True

print(Solution().isAnagram("bob","bob"))
print(Solution().isAnagram("bob","bo"))
print(Solution().isAnagram("anagram","nagaram"))
print(Solution().isAnagram("anagram","margana"))
print(Solution().isAnagram("rat","car"))
print(Solution().isAnagram("rat","carr"))
print(Solution().isAnagram("",""))
