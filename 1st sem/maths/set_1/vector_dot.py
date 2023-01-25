import numpy as np
print("enter the first vector")
x = [int(x) for x in input().split()]
print(x)
print("enter the second vector")
n = [int(n) for n in input().split()]
v1 = np.array(x)
v2 = np.array(n)
dot_product = np.dot(v1, v2)
print("dot product of vectors",dot_product)