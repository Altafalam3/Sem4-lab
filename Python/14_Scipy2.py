import numpy as np
from scipy.linalg import inv, det, kron

# Define matrix A
A = np.array([[5, 3, 2], [6, 9, -3], [1, 7, 4]])

# Define matrix B
B = np.array([[3, -1], [2, -5]])

# a. Find inverse of matrix A
A_inv = inv(A)
print("Inverse of A:\n", A_inv)

# b. Find Kronecker product of A with B
AB_kron = kron(A, B)
print("Kronecker product of A and B:\n", AB_kron)

# c. Find determinant of matrix A
A_det = det(A)
print("Determinant of A:", A_det)
