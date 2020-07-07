# 16.5

# my solution:
def zeroes(n):
    # return number of trailing zeroes of n!
    count = 0

    while n >= 5:
        count += fiveCounter(n)
        n -= 1

    return count

def fiveCounter(n):
    if n > 0 and n % 5 == 0:
        return 1 + helper(n / 5)
    else:
        return 0

# an arguably more concise solution:
def countFactZeroes(n):
    count = 0

    if n < 0:
        return -1

    i = 5

    while n / i > 0:
        count += n // i
        i *= 5

    return count
