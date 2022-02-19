def minmax2(array_of_integers):
    if len(array_of_integers) <= 1:
        return "Insufficient array size"
    if array_of_integers[0] > array_of_integers[1]:
        min1 = max2 = array_of_integers[1]
        min2 = max1 = array_of_integers[0]
    else:
        min1 = max2 = array_of_integers[0]
        min2 = max1 = array_of_integers[1]
    for i in range(1, len(array_of_integers)):
        if array_of_integers[i] > max2:
            if array_of_integers[i] > max1:
                max2 = max1
                max1 = array_of_integers[i]
            elif array_of_integers[i] < max1:
                max2 = array_of_integers[i]
        if array_of_integers[i] < min2:
            if array_of_integers[i] < min1:
                min2 = min1
                min1 = array_of_integers[i]
            elif array_of_integers[i] > min1:
                min2 = array_of_integers[i]
    return [max2, min2]

print(minmax2([1,2,3,4]))
print(minmax2([1,2,3,4,5]))
print(minmax2([4,3,2,1]))
print(minmax2([2,2,1,1]))
print(minmax2([1,1,1,1]))
print(minmax2([1,2]))
print(minmax2([2,1]))
