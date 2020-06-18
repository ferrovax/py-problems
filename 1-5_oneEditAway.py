# 1.5 One Away
def oneEditAway(str1, str2):
	if abs(len(str1) -len(str2)) > 1:
		return False
	# Get shorter and longer strings
	s1 = str1 if len(str1) < len(str2) else str2
	s2 = str2 if len(str1) < len(str2) else str1

	index1, index2, foundDifference = 0, 0, False

	while index1 < len(s1) and index2 < len(s2):
		if s1[index1] != s2[index2]:
			if foundDifference:
				return False
			foundDifference = True
			if len(s1) == len(s2):
				# On replace (not insert or delete) move 'shorter' pointer
				index1 += 1
		else:
			# matching characters, so we move the shorter pointer forward
			index1 += 1
		# always move the longer string's pointer along
		index2 += 1
	return True
