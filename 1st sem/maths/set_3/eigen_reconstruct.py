import numpy as np
from numpy import diag
from numpy import dot
from numpy.linalg import inv
from numpy.linalg import eig


matrix = np.array([[3, 1], [2, 2]])
eigen_value, eigen_vector = np.linalg.eig(matrix)
print("eigen value :",eigen_value)
print("eigen vector :\n",eigen_vector)
inv = inv(eigen_vector)
diag = diag(eigen_value)
rmatrix = eigen_vector.dot(diag).dot(inv)

print("reconstructed matrix :")
for row in rmatrix:
    print(row)