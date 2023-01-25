import numpy as np
matrix = np.array([[2, 2, 1], [3, 4, 8],[12, 4, 0]])
inverse = np.linalg.inv(matrix)
print(inverse)