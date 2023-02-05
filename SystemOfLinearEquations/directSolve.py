''' Solving system of linear equations directly using numpy library '''

import numpy as np
a = np.array([[2, -1, 5, -3],
           [4, 1, 2, -1],
           [4, 1, -3, -8],
           [3, 6, -1, 2]],float)
b = np.array([3, 2, 2, -1], float)

x = np.linalg.solve(a,b)
print(x)
