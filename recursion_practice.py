from array import array
import math
from multiprocessing.dummy import Array

# def convertIntegerString(target_string, index_from_last, latest_string):
#     if len(target_string) == index_from_last: return latest_string
#     return convertIntegerString(
#         target_string,
#         index_from_last + 1,
#         target_string[len(target_string) - index_from_last - 1] + ("," if (index_from_last != 0 and index_from_last % 3 == 0) else "") + latest_string
#     )

# print(convertIntegerString("13531", 0, ""))


# def harmonicSum(target, curr, cumul):
#     if curr == target:
#         return cumul  + 1 / curr
#     return harmonicSum(target, curr + 1, cumul + 1 / curr)

# print(harmonicSum(10, 1, 0))

# def power(x, n):
#     pow = 1
#     while n > 0:
#         if n % 2 == 1:
#             n -= 1
#             pow = pow * x
#         n = n / 2
#         x = x * x
#     return pow

# print(power(5, 11))

# def powerRecursive(x, n):
#     if n == 0:
#         return 1
#     partial = powerRecursive(x, n/2)
#     result = partial * partial
#     if n % 2 == 1:
#         result *= x
#     return result

# print(power(5, 7))


# def recursive2dArraySum(arr: array, array_x: int, array_y: int, sum: int):
#     if array_y == 0 and array_x == 0:
#         return sum
#     if array_y == 0:
#         array_x -= 1
#         array_y = len(arr[0])
#     return recursive2dArraySum(arr, array_x, array_y - 1, sum + arr[array_x][array_y - 1])

# print(recursive2dArraySum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2, 3, 0))


# def recursiveLog(x, ans):
#     if x == 2:
#         return ans
#     if x < 2:
#         return ans - 1
#     return recursiveLog(x / 2, ans + 1)

# print(recursiveLog(8, 1))


# def recursiveElementUnique(arr, index_current, index_search):
#     if arr[index_current] == arr[index_search] and index_current != index_search:
#         return True
#     if index_search == len(arr) - 1:
#         index_search = 0
#         index_current += 1
#     if index_current == len(arr) - 1:
#         return False
#     return recursiveElementUnique(arr, index_current, index_search + 1)

# print(recursiveElementUnique([1, 2, 3, 4], 0, 0))
# print(recursiveElementUnique([1, 2, 3, 1], 0, 0))
# print(recursiveElementUnique([2, 5, 3, 1], 0, 0))
# print(recursiveElementUnique([2, 2, 3, 1], 0, 0))

# def recursiveProductNoMultiplication(x, y, cumul):
#     if y == 0:
#         return cumul
#     return recursiveProductNoMultiplication(x, y - 1, cumul + y)

# print(recursiveProductNoMultiplication(5, 9, 0))

# def findAllSubsets(input: array, index: int, latest: array, cumul: array):

#     if index == len(input):
#         index = 0
#         latest = latest + [input[index]]

#     if len(cumul) == 16:
#         return cumul

#     return findAllSubsets(input, index + 1, latest, cumul + [latest + [input[index]]])


# print(findAllSubsets([1, 2, 3, 4], 0, [1], []))

# def palindrome(string, index):
#     if string[index] != string[len(string) - index - 1]:
#         return False
#     if index == math.floor(len(string)/2):
#         return True
#     return palindrome(string, index + 1)

# print(palindrome("abcba", 0))
# print(palindrome("a", 0))
# print(palindrome("abb", 0))

# def recursiveArrayCheck(arr, index1, index2, index3):
#     if arr[index1] + arr[index2] == arr[index3] and index1 != index2 != index3:
#         return True

#     if index1 == index2 == index3 == len(arr) - 1:
#         return False

#     if index1 == index2 == len(arr) - 1:
#         index1 = 0
#         index2 = 0
#         index3 += 1

#     elif index1 == len(arr) - 1:
#         index1 = 0
#         index2 += 1

#     return recursiveArrayCheck(arr, index1 + 1, index2, index3)

# print(recursiveArrayCheck([1,2,3,4],0,0,0))
# print(recursiveArrayCheck([1,9,9,2],0,0,0))
# print(recursiveArrayCheck([-5,5,0,1],0,0,0))
# print(recursiveArrayCheck([1,1,1,1],0,0,0))
# print(recursiveArrayCheck([1,1,1,2],0,0,0))
# print(recursiveArrayCheck([1,1,1,2],0,0,0))
# print(recursiveArrayCheck([1,3,4,9],0,0,0))

def hanoi(n, start, end, pegs):
    if pegs is None:
        pegs = [list(range(1,n+1,1)), list(), list()]
        print(pegs)
    if n == 1:
        print(start,'->',end)
        popped_peg = pegs[start-1].pop(0)
        pegs[end-1].insert(0,popped_peg)
        print(pegs)
    else:
        other = 6 - start - end

        hanoi(n - 1, start, other, pegs)
        print(start,'->', end)
        popped_peg = pegs[start-1].pop(0)
        pegs[end-1].insert(0,popped_peg)
        print(pegs)

        hanoi(n - 1, other, end, pegs)

hanoi(3, 1, 3, pegs=None)

# def Hanoi(n,start_,inter_,end_, pegs=None):  # new optional argument
#     if pegs is None:
#         pegs = [start_, inter_, end_]  # build a list of lists if one was not passed in
#     if n==1:
#         end_.append(start_.pop()) # using pop makes this much easier
#         print('start_peg, inter_peg, end_peg :{}\t{}\t{}'.format(*pegs)) # prints in order
#     else:
#         Hanoi(n-1,start_,end_,inter_, pegs) # pass on the list of lists in each recursive call
#         Hanoi(1,start_,inter_,end_, pegs)   # this lets the original order be preserved
#         Hanoi(n-1,inter_,start_,end_, pegs)
# n=3
# A=list(range(n,0,-1))
# B,C=[],[]
# Hanoi(n, A, B, C)
