import numpy as np
from numpy.linalg import norm
a = np.array([2,1,2,3,2,9])
b = np.array([3,4,2,4,5,5])
print("A:", a)
print("B:", b)
cosine = np.dot(a,b)/(norm(a)*norm(b))
print("Cosine Similarity:", cosine)
