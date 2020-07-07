# 5.5
# Explain what ( n & ( n - 1 ) ) == 0 does.

# n & (n - 1) == 0 is true if n is a power of 2

def isPowerOfTwo(n):
    return n & (n - 1) == 0

print(isPowerOfTwo(128)) #True
print(isPowerOfTwo(1)) #True
print(isPowerOfTwo(42)) #False

# NOTE: returns True for n = 0.
