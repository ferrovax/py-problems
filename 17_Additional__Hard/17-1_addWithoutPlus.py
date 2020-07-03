# 17.1

def add(x, y):
    if y == 0:
        return x

    sum = x ^ y
    carry = (x & y) << 1

    return add(sum, carry)
