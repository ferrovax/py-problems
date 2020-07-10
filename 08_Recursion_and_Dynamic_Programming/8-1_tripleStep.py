# 8.1
# classic staircase problem, n stairs, 1, 2, or 3 steps at a time

def memoTripleStep(n):
    cache = [-1]*(n + 1)

    return count(n, cache)

def count(n, cache):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif cache[n] > -1:
        return cache[n]
    else:
        cache[n] = count(n - 1, cache) + count(n - 2, cache) + count(n - 3, cache)
        return cache[n]
