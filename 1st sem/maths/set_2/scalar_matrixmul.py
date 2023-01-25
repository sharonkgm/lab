import numpy as np
r = int(input("enter the number of rows"))
c = int(input("enter the number of columns"))
s = int(input("enter the scalar element"))
print("enter",r*c,"elements")
elements = list(map(int,input().split()))
matrix = np.array(elements).reshape(r,c)
m = matrix * s
print(m)
