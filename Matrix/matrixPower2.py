############################################################
######  Power of a Matrix (Using Python Functions)   #######
############################################################
""" 
In python interpreter type :-

In [22]: import numpy
In [23]: dir(numpy.linalg)

"""

import numpy as np
A = np.array([[2,2],[2,-1]])
print(np.linalg.matrix_power(A, 10))