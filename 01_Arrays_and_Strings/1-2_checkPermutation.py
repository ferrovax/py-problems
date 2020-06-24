# 1.2 Check Permutation
def checkPermutation(str1, str2):
	# Could sort them then return whether equal
	# or do the following (which is faster):
	
	counts = [0]*128

	for c in str1:
		i = int(c)
		counts[i] += 1

	for c in str2:
		i = int(c)
		counts[i] -= 1
		if counts[i] < 0:
			return False

	return True
