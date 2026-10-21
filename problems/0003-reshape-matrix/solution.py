import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	reshaped_matrix = []
	total_elements = 0
	elements = []
	for row in a:
		for element in row:
			total_elements += 1
			elements.append(element)
	new_total_elements = 1
	for x in new_shape:
		new_total_elements *= x
	k = 0
	if total_elements == new_total_elements:
		for _ in range(new_shape[0]):
			row = []
			for _ in range(new_shape[1]):
				row.append(elements[k])
				k += 1
			reshaped_matrix.append(row)

	return reshaped_matrix