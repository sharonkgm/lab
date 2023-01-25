import numpy as np
arr = np.matrix([[9, 8, 2],
                 [5, 4, 6],
                 [9, 2, 1]])
#extracting diagonal elements
arr2 = np.diag(arr)
print(arr2)
print("\n")
r = np.diag(arr2)
print(r)