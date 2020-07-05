# 10.1
# merge two sorted arrays

def merge(A, B):
    # start at the ends
    index1, index2 = len(A) - 1, len(B) - 1

    A += [None] * len(B)
    index3 = len(A) - 1

    while index2 >= 0:
        if index1 >= 0 and A[index1] > B[index2]:
            A[index3] = A[index1]
            index1 -= 1
        else:
            A[index3] = B[index2]
            index2 -= 1

        index3 -= 1

    return A

# A = [2, 13, 17, 24, 56, 88, 102]
# B = [-3, 5, 20, 33, 74]

# C = merge(A, B)

# print(C)
