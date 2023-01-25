import matplotlib.pyplot as plt
import numpy as np

matrix = np.array([[1,40],[5,26],[10,88],[4,10],[7,67]])
x, y = np.split(matrix,2,axis=1)
plt.scatter(x, y)
plt.show()
