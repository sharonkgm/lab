import numpy as np
r = int(input("enter the number of rows :"))
c = int(input("enter the number of columns :"))
print("enter",r*c,"elements :")
elements = list(map(int,input().split()))
matrix = np.array(elements).reshape(r,c)
vector = np.array([2,2,2])
a = np.dot(matrix,vector)
print(a)