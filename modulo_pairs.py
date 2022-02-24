import math as mt

def findDivisors(n):

    v = []

    for i in range(1, mt.floor(n**(.5)) + 1):
        if (n % i == 0):

            if (n / i == i):
                v.append(i)
            else:
                v.append(i)
                v.append(n // i)

    return v

def printPairs(arr, n, k):

    occ = dict()
    for i in range(n):
        occ[arr[i]] = True

    isPairFound = False

    for i in range(n):

        if (occ[k] and k < arr[i]):
            print("(", k, ",", arr[i], ")", end = " ")
            isPairFound = True

        if (arr[i] >= k):

            v = findDivisors(arr[i] - k)

            for j in range(len(v)):
                if (arr[i] % v[j] == k and
                    arr[i] != v[j] and
                    occ[v[j]]):
                    print("(", arr[i], ",", v[j],
                                       ")", end = " ")
                    isPairFound = True

    return isPairFound

arr = [3, 1, 2, 5, 4]
n = len(arr)
k = 2

if (printPairs(arr, n, k) == False):
    print("No such pair exists")
