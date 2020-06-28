# 5.1
# EXAMPLE
# Input:    N = 10000000000, M = 10011, i = 2, j = 6
# Output:   N = 10001001100

# NOTE: Allowed to assume M fits between bits i and j

def insertBits(n, m, i, j):
    # comments walk through the above example

    ones = ~0
    # 1111 1111 1111 1111 1111 1111 1111 1111

    left = ones << (j + 1)
    right = (1 << i) - 1
    # left  = ...1111 1000 0000
    # right = ...0000 0000 0011

    mask = left | right
    # mask = ...1111 1000 0011

    n = n & mask
    m = m << i
    # n = 0100 0000 0000
    # m = 0000 0100 1100

    return n | m
    # n|m = 10001001100
