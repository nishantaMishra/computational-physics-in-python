##############################################################
###############   Tenth power of Matrix    ###################
##############################################################
"""Calculating power of a Matrix by Singularity Transformation """

import numpy as np
import scipy.linalg as la

P = np.array([[2,2],[2,-1]])
#print(P)
results = la.eig(P)
print('\nEigen values are \n',results[0])
print('\nEigen vectors are \n',results[1])

D = np.diag(results[0])
#print(D) 
Pinv = la.inv(P)
M = P @ D**10 @ Pinv 
print('\nMatrix to the power ten is \n',M) 
