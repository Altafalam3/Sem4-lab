def vandermonde_matrix(arr, p, ascending=False):
    n = len(arr)
    matrix = []
    for i in range(n):
        row = []
        for j in range(p):
            if ascending:
                row.append(arr[i]**j)
            else:
                row.append(arr[i]**(p-j-1))
        matrix.append(row)
    return matrix

matrix = vandermonde_matrix([1, 2, 3], 3, True)
print(matrix)
