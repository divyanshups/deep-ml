def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	rows = 0
	cols = 0
	for row in matrix:
		rows += 1
		cols = 0
		for element in row:
			cols += 1
	

	if mode == "row":
		total = 0
		for row in matrix:
			total += sum(row)
		
			means.append(total/cols)
			total = 0

	else:
		total = 0
		for j in range(cols):
			for i in range(rows):
				total += matrix[i][j]
			means.append(total/rows)
			total = 0

		
	return means