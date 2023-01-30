from numpy import array
from numpy.linalg import norm
#L2 norm = sum of square root of elements
a = array([25, 2, 5])
nm = norm(a,2)
print(nm)
