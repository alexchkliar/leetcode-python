def isPalindrome(str):
    stack = []
    for i in range(0, len(str)):
        stack.append(str[i])
    for i in range(0, len(stack)):
        char = stack.pop()
        if char != str[i]:
            return False
    return True

print(isPalindrome("racecar"))
print(isPalindrome("bob"))
print(isPalindrome("aa"))
print(isPalindrome("wat"))
print(isPalindrome("hey"))
