# 1.7 Rotate Matrix
def rotate(matrix):
	# proceed by layer, swapping index by index
	# first and last set the range on indices at each layer depth
	# offset is for iterating through the two backwards-direction sides in order
	n = len(matrix)

	if n == 0 or n != len(matrix[0]):
		# empty or not square
		return False

	for layer in range(n // 2):

		first = layer
		last = n - 1 - layer

		for i in range(first, last):
			offset = i - first

			# top @ matrix[first][i], or can be thought of as matrix[layer][i]
			# left @ matrix[last - offset][first], or matrix[last - offset][layer]
			# bottom @ matrix[last][last - offset]
			# right @ matrix[i][last]

			# save the top
			top = matrix[first][i]

			# top = left
			matrix[first][i] = matrix[last - offset][first]

			# left = bottom
			matrix[last - offset][first] = matrix[last][last - offset]

			# bottom = right
			matrix[last][last - offset] = matrix[i][last]

			# right = top
			matrix[i][last] = top

	return True

#  [ 0,  1,  2,  3
#    4,  5,  6,  7
#    8,  9, 10, 11
#   12, 13, 14, 15 ]

#	=============>

# [ 12,  8,  4,  0
#   13,  9,  5,  1
#   14, 10,  6,  2
#   15, 11,  7,  3 ]
