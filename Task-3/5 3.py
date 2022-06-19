import numpy as np
A = np.array([[10,2,35], [4,57,69]])
B = np.array([[2,4,6], [8,9,0], [3,2,1]])
print("Matrix A is:\n",A)
print("Matrix B is:\n",B)
C = np.matmul(A,B)
print("Matrix multiplication of matrix A and B is:\n",C)
