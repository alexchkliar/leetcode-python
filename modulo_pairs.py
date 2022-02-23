import math as mt

def findDivisors(n):

    v = []

    # Vector is used to store the divisors
    for i in range(1, mt.floor(n**(.5)) + 1):
        if (n % i == 0):

            # If n is a square number, push
            # only one occurrence
            if (n / i == i):
                v.append(i)
            else:
                v.append(i)
                v.append(n // i)

    return v

# Function to find pairs such that (a%b = k)
def printPairs(arr, n, k):

    # Store all the elements in the map
    # to use map as hash for finding elements
    # in O(1) time.
    occ = dict()
    for i in range(n):
        occ[arr[i]] = True

    isPairFound = False

    for i in range(n):

        # Prall the pairs with (a, b) as
        # (k, numbers greater than k) as
        # k % (num (> k)) = k i.e. 2%4 = 2
        if (occ[k] and k < arr[i]):
            print("(", k, ",", arr[i], ")", end = " ")
            isPairFound = True

        # Now check for the current element as 'a'
        # how many b exists such that a%b = k
        if (arr[i] >= k):

            # find all the divisors of (arr[i]-k)
            v = findDivisors(arr[i] - k)

            # Check for each divisor i.e. arr[i] % b = k
            # or not, if yes then prthat pair.
            for j in range(len(v)):
                if (arr[i] % v[j] == k and
                    arr[i] != v[j] and
                    occ[v[j]]):
                    print("(", arr[i], ",", v[j],
                                       ")", end = " ")
                    isPairFound = True

    return isPairFound

# Driver Code
arr = [3, 1, 2, 5, 4]
n = len(arr)
k = 2

if (printPairs(arr, n, k) == False):
    print("No such pair exists")

# This code is contributed by mohit kumar
