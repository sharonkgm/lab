import numpy as np

matrix = np.array([[3, 1], [2, 2]])
eigen_value, eigen_vector = np.linalg.eig(matrix)

print(eigen_value)
print(eigen_vector)