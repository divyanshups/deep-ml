def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    transposed_matrix = []
    rows = 0
    for row in a:
        cols = 0
        for element in row:
            cols += 1
        rows +=1
    for i in range(rows):
        for j in range(cols):
            if i == 0:
                new_arr = []
                new_arr.append(a[i][j])
                transposed_matrix.append(new_arr)
            else:
                transposed_matrix[j].append(a[i][j])

            
    return transposed_matrix