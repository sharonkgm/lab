import numpy as np
print("enter the first vector")
x = [int(x) for x in input().split()]
print(x)
print("enter the second vector")
n = [int(n) for n in input().split()]
print(n)
v1 = np.array(x)
v2 = np.array(n)
crossp = np.cross(v1, v2)
print("cross product of vectors", crossp)

