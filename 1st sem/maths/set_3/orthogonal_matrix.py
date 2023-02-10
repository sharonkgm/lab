import numpy as np
def isorthogonal(matrix,m,n):
    for i in range(0, n):
        for j in range(0, n):
            sum = 0
            for k in range(0, n):
                sum = sum + (matrix[i][k] *
                             matrix[j][k])
    if (i == j and sum != 1):
        return False
    if (i != j and sum != 0):
        return False
    return True

matrix = np.array([[1, 0, 0],[0, 1, 0],[0, 0, 1]])

if(isorthogonal(matrix, 3, 3)):
    print("given matrix is orthogonal ,QQ^t = Q^t Q = I ")
else:
    print("given matrix is not orthogonal, QQ^t != Q^t Q != I ")
