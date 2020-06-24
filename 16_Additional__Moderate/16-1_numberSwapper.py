# 16.1 Number Swapper
# no temp

def swap(a, b):
    if a > b:
        return swapper(a, b)
    else:
        return swapper(b, a)

def swapper(bigger, smaller):
    bigger -= smaller
    smaller += bigger
    bigger = smaller - bigger

    return bigger, smaller
