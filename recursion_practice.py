from array import array
import math

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


def recursive2dArraySum(arr: array, array_x: int, array_y: int, sum: int):
    # init_x = array_x
    # init_y = array_y
    if array_y == 0 and array_x == 0:
        return sum + arr[0][0]
    # if array_x == 0:
        # return sum + arr[0][array_y]

    return recursive2dArraySum(arr, array_x, array_y - 1, sum + arr[array_x][array_y])
    return recursive2dArraySum(arr, array_x - 1, array_y, sum + arr[array_x][array_y])
    # if array_x != 0:
    #     return sum + recursive2dArraySum(arr[array_x - 1][array_y])
    # return sum + recursive2dArraySum(arr[array_x][array_y - 1])

T = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(T[0][1])
print(recursive2dArraySum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2, 2, 0))
