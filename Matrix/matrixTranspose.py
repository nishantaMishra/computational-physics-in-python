###################################################################
####################    Transpose of a Matrix    #####################
##############################################################
""" Program to transpose a matrix using a nested loop """
import numpy as np
X = [[12, 7],
     [4 ,5],
     [3 ,8]]

result = np.zeros((len(X[0]), len(X)))

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

print(result)
