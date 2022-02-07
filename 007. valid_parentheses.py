class Solution(object):
    def isValid(self, s):
        stack = []
        opening_characters = ["(","[","{"]
        closing_characters = [")","]","}"]

        for char in s:
            if char in closing_characters and stack == []:
                return False
            if char in opening_characters:
                stack.append(char)
            else:
                if stack[-1] != opening_characters[closing_characters.index(char)]:
                    return False
                # else:
                stack.pop(-1)
        if len(stack) > 0:
            return False
        return True



print(Solution().isValid("()"))
print(Solution().isValid("["))
print(Solution().isValid("()[]{}"))
print(Solution().isValid("(]"))
print(Solution().isValid("["))
