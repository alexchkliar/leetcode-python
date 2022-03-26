def quickSortInPlace(S, a, b):
    if a >= b: return
    left = a
    right = b-1
    pivot = S[b]
    while left <= right:
        while left <= right and S[left] < pivot: left+=1
        while left <= right and S[right] > pivot: right-=1
        if left <= right:
            temp = S[left]
            S[left] = S[right]
            S[right] = temp
            left += 1
            right -= 1
    temp = S[left]
    S[left] = S[b]
    S[b] = temp
    quickSortInPlace(S, a, left - 1)
    quickSortInPlace(S, left + 1, b)


arr = [3,2,1,5,4,6,7,5,4,3,8,9,15,1]
quickSortInPlace(arr, 0, len(arr) - 1)
print(arr)
