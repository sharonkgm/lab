import numpy as np
arr = np.matrix([[9, 8, 2],
                 [5, 4, 6],
                 [9, 2, 1]])

arr2 = np.diag(arr)
print("diagonal elements :",arr2)
print("\n")
r = np.diag(arr2)
print("diagonal matrix :\n",r)