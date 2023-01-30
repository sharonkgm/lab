import numpy as np
r = int(input("enter the number of rows :"))
c = int(input("enter the number of columns :"))
print(f'enter {r*c} elements')
elements = list(map(int,input().split()))
matrix = np.array(elements).reshape(r,c)
count = 0
for i in range(r):
    for j in range(c):
        if matrix[i][j] != 0:
            count = count + 1
sparsity = 1.0 - float( count / (r*c) )
print("sparsity of the given matrix is :",sparsity)