# Give a recursive algorithm to compute the product of two positive integers, m and n, using only addition and subtraction.

# implementation
from msvcrt import kbhit


def product_positive_integers(a, b, c):
    if b == 0:
        return c
    return product_positive_integers(a, b - 1, c + a)

# testing
print(product_positive_integers(5,8,0))
print(product_positive_integers(9,9,0))
print(product_positive_integers(1,10,0))
print(product_positive_integers(99,99,0))
