# 1.6 String Compression
def stringCompression(s):
	# aabcccccaaa -> a2b1c5a3, returns original if compression is shorter
	# in Java, using a string builder would be a good idea, but here ''.join(sequenceOfStrings) is likely fast enough
	countConsecutive = 0
	compressedString = []

	for i in range(len(s)):
		countConsecutive += 1
		if i + 1 >= len(s) or s[i] != s[i + 1]:
			compressedString.append(s[i] + str(countConsecutive))
			countConsecutive = 0

	return ''.join(compressedString) if len(compressedString) < len(s) else s
