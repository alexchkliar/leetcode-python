class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""

        common = ""
        min_len = len(strs[0])
        for i in range(0,len(strs)):
            if len(strs[i]) < min_len:
                min_len = len(strs[i])

        for i in range(0, min_len):
            flag = True
            init_letter = strs[0][i]
            for j in range(0,len(strs)):
                if strs[j][i] != init_letter:
                    flag = False
                    break
            if flag:
                common += init_letter
            else:
                break

        return common

arr1 = []
arr2 = [""]
arr3 = ["carrot", "car", "cart"]
arr4 = ["app", "apple", "api"]
arr5 = ["a", "a", "a"]
arr6 = ["a", "b", "ccc"]

print(Solution().longestCommonPrefix(arr1))
print(Solution().longestCommonPrefix(arr2))
print(Solution().longestCommonPrefix(arr3))
print(Solution().longestCommonPrefix(arr4))
print(Solution().longestCommonPrefix(arr5))
print(Solution().longestCommonPrefix(arr6))
