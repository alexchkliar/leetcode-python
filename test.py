# n = 10
# i_count = 0
# j_count = 0
# k_count = 0
# l_count = 0
# m_count = 0

# for i in range(0,n):
#     i_count += 1
#     for j in range(i,n):
#         j_count += 1
#         for k in range(j,n):
#             k_count += 1
#             for l in range(k,n):
#                 l_count += 1
#                 for m in range(l,n):
#                     m_count += 1
# print(i_count)
# print(j_count)
# print(k_count)
# print(l_count)
# print(m_count)

# def reverseRecursive(str, index, output):
#     if index == len(str):
#         return output
#     return reverseRecursive(str, index + 1, output + str[len(str) - index - 1])


# print(reverseRecursive("ab", 0, ""))
# print(reverseRecursive("abcde", 0, ""))

# def reverseIterative(str):
#     reversed_str = ""
#     for i in range(0,len(str)):
#         reversed_str += str[len(str) - 1 - i]
#     return reversed_str

# print(reverseIterative("ab"))
# print(reverseIterative("abcde"))

# def fizzBuzz(integers):
#     for i in range(0, integers + 1):
#         if i % 5 == 0 and i % 3 == 0: print("FizzBuzz")
#         elif i % 3 == 0: print("Fizz")
#         elif i % 5 == 0: print("Buzz")
#         else: print(i)

# fizzBuzz(25)

def testLoop(n):
    count=0
    k=n
    i=1
    j=1
    while k >= 1:
        while i <= 1000:
            while j<=n:
                count+=1
                i=i*2
                j=j+2
                k=k/4
    return count

print("test")
print(testLoop(2))
print("test")
# print(testLoop(100))
# print(testLoop(1000))
# print(testLoop(10000))
