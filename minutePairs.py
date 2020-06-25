# Problem:
# Given an array of numbers, find how many pairs sum to a number evenly
# divisible by sixty.

# Examples:
#
# An input of [3, 60, 60, 60] returns 3 because three pairs, all (60, 60) in
# this case, sum to a number evenly divisible by sixty.
#
# An input of [10, 50, 30, 90, 4] returns 2 because two pairs, (10, 50) and
# (30, 90), sum to numbers evenly divisible by sixty.

# NOTE: The premise of this problem had something to do with time management.

def solution(array):
    unique_nums = set(array)
    counts = {}

    biggest = -1
    num_pairs = 0

    for index in range(len(array)):
        num = array[index]

        if num in counts.keys():
            counts[num] += 1
        else:
            counts[num] = 1

        biggest = max(biggest, num)

    while unique_nums:
        num = unique_nums.pop()
        count = counts[num]

        complement = 60 - (num % 60)

        while complement <= biggest:
            if complement == num:
                num_pairs += int( count * (count - 1) / 2 )
            elif complement in unique_nums:
                num_pairs += count * counts[complement]

            complement += 60

    return num_pairs

# print(solution([3, 60, 60, 60]) == 3)
# print(solution([10, 50, 30, 90, 4]) == 2)
