# 1.8 Zero Matrix
def zero(matrix):
	# zero rows and columns that contain any 0s
	
	rows_with_zeroes = [0] * len(matrix)
	columns_with_zeroes = [0] * len(matrix[0])

	for i in range(len(matrix)):
		for j in range(len(matrix[0])):

			if matrix[i][j] == 0:
				rows_with_zeroes[i] = 1
				columns_with_zeroes[j] = 1

	for i in range(len(matrix)):
		for j in range(len(matrix[0])):

			if rows_with_zeroes[i] or columns_with_zeroes[j]:
				matrix[i][j] = 0
