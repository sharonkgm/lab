from numpy import array
from numpy.linalg import norm
#L1 norm = sum of |a|
a = array([25, 2, 5])
nm = norm(a,1)
print("L1 norm :",nm)

