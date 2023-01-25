from numpy import inf,array
from numpy.linalg import norm

a = array([25, 2, 5])
nm = norm(a, inf)
print(nm)
