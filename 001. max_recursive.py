# inputs: a array, b index of array initialized at 0, c initialized max value (value of first element of array)
# returns max value of array a
# time complexity: O(n) -- we memoize the maximum

def max(a, b, c):
    if b == len(a):
        return c
    if a[b] > c:
        return max(a, b + 1, a[b])
    else:
        return max(a, b + 1, c)

a = [1,2,3,4,5]
b = [4,3,7,0,1]
c = [8,4,3,2,-1]
print(max(a, 0, a[0]))
print(max(b, 0, b[0]))
print(max(c, 0, c[0]))
