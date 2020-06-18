# 1.7 Rotate Matrix
def rotate(matrix):
	# proceed by layer, swapping index by index; first and last set range on indices at each layer depth, offset is for iterating through the two 'backwards'-direction sides in order
	n = len(matrix)

	if n == 0 or n != len(matrix[0]):
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
			top = matrix[first][i]										# save the top
			matrix[first][i] = matrix[last - offset][first]				# top = left
			matrix[last - offset][first] = matrix[last][last - offset]	# left = bottom
			matrix[last][last - offset] = matrix[i][last]				# bottom = right
			matrix[i][last] = top										# right = top

	return True
