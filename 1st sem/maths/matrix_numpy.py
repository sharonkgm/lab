import numpy as np
r = int(input("enter the number of rows"))
c = int(input("enter the number of columns"))
print("enter the elements")
elements = list(map(int,input().split()))
matrix = np.array(elements).reshape(r,c)
print(matrix)