import numpy as np
print("enter the first vector")
x = [int(x) for x in input().split()]
print(x)
print("enter the second vector")
n = [int(n) for n in input().split()]
v1 = np.array(x)
v2 = np.array(n)
divide = np.divide(v1, v2)
print("division of vectors",divide)