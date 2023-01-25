import numpy as np
print("enter the first vector :")
x = [int(x) for x in input().split()]
print(x)
n = int(input("enter a scalar value :"))
print(n)
v1 = np.array(x)
mul = n*v1
print("vector scalar multiplication :", mul)
