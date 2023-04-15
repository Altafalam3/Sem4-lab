import numpy as np
from scipy.linalg import solve

# Create coefficient matrix
A = np.array([[9, 6, -5, 2], [4, 5, -7, 3], [-3, -4, 2, -5], [6, 1, 9, -1]])

# Create constant matrix
B = np.array([17, 10, 20, 23])

# Solve the system of linear equations
X = solve(A, B)

# Print the solution
print("Solution: x = {}, y = {}, z = {}, w = {}".format(X[0], X[1], X[2], X[3]))
