import math

def merge(arr1, arr2):
    output = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            output += [arr1[i]]
            i+=1
        else:
            output += [arr2[j]]
            j+=1
    while i < len(arr1):
        output += [arr1[i]]
        i+=1
    while j < len(arr2):
        output += [arr2[j]]
        j+=1

    return output

def mergeSort(arr):
    n = len(arr)
    if n < 2: return arr
    a1 = arr[0: math.floor(len(arr)/2)]
    a2 = arr[math.floor(len(arr)/2): len(arr)]

    s1 = mergeSort(a1)
    s2 = mergeSort(a2)
    return merge(s1, s2)

def quickSort(arr, left, right):
    pivotIndex = right
    leftIndex = left
    rightIndex = right - 1
    if leftIndex >= rightIndex:
        return

    while leftIndex <= rightIndex:
        while leftIndex <= rightIndex and arr[leftIndex] < arr[pivotIndex]: leftIndex += 1
        while leftIndex <= rightIndex and arr[rightIndex] > arr[pivotIndex]: rightIndex -= 1
        if leftIndex <= rightIndex:
            temp = arr[leftIndex]
            arr[leftIndex] = arr[rightIndex]
            arr[rightIndex] = temp
            leftIndex += 1
            rightIndex -= 1
    temp = arr[leftIndex]
    arr[leftIndex] = arr[pivotIndex]
    arr[pivotIndex] = temp

    quickSort(arr, left, leftIndex - 1)
    quickSort(arr, leftIndex + 1, right)

arr1 = [1, 3, 2, 5, 4, 7, 1, 9]
quickSort(arr1, 0, len(arr1) - 1)
print(arr1)
