import numpy as np
n_array = np.array([[2, 2, 1], [3, 4, 8],[12, 4, 0]])
print("Numpy Matrix is:")
print(n_array)
det = np.linalg.det(n_array)
print("\nDeterminant of given matrix:")
print(int(det))
