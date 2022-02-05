# inputs: array a, index of array b
# outputs: integer value of first pair in array, or alert that there are no pairs in the array if indeed there are none

# implementation
def repeated_pair_index(a, b):
    if b == len(a) - 1:
        return "No pairs in array"
    if a[b] == a[b + 1]:
        return a[b]
    return repeated_pair_index(a, b + 1)

# testing
a = [1,2,3,3,4,4,5]
b = [4,3,7,0,1]
c = [8,4,-1,-1,5]
print(repeated_pair_index(a, 0))
print(repeated_pair_index(b, 0))
print(repeated_pair_index(c, 0))
