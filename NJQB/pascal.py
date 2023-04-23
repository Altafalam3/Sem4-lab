def pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
        triangle.append(row)

    # Determine maximum number of digits for formatting
    max_digits = len(str(triangle[-1][len(triangle[-1])//2]))
    
    # Print triangle with proper spacing
    for row in triangle:
        for num in row:
            print(f"{num:^{max_digits}}", end=" ")
        print()

# example usage
pascal_triangle(5)
