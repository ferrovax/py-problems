# Foobar (level 3 difficulty)
# Find how many lucky triples there are in any given sorted list, where a lucky
# triple consists of list[i], list[j], and list[k] such that list[i] divides
# list[j] and list[j] divides list[k].

# EXAMPLES:
# solution([1, 2, 3, 4, 5, 6])
#   => 3 ((1, 2, 4), (1, 2, 6), (1, 3, 6))
# solution([1, 1, 1])
#   => 1 ((1, 1, 1))

def solution(l):
    # consider lucky triple (x, y, z) and 'pivot' around y

	total, i = 0, len(l)-1

	while i > 0:
		total += find_Xs(l[:i], l[i]) * find_Zs(l[i+1:], l[i])
		i -= 1

	return total

def find_Xs(left_l, y):
	return len([x for x in left_l if y % x == 0])

def find_Zs(right_l, y):
	return len([z for z in right_l if z % y == 0])

# print(solution([1, 2, 3, 4, 5, 6]) == 3)
# print(solution([1, 1, 1]) == 1)
