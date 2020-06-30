# 5.6
# Determine the number of bit-flips needed to convert int a to int b.

def numBitFlips(a, b):
    num, xor = 0, a ^ b

    while xor != 0:
        num += 1

        xor = xor & (xor - 1)

    return num
