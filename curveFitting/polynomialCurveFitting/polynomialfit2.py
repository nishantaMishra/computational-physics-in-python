#######################################################################
############    Polynomial Curve Fitting (Taking User Input)      ############
######################################################################

""" Fit a quadratic polynomial in data
x = [0, 1, 2, 3, 4, 5]
y = [2, 8, 14, 28, 39, 62]
"""  
import numpy as np 

nop = int(input("Enter the number of points: "))
#--------------------------
x = np.array([])
y = np.array([])
for i in range(nop):
    x = np.append(x, float(input("x[{}]: ".format(i))))
for i in range(nop):
    y = np.append(y, float(input("y[{}]: ".format(i))))
#--------------------------
m = len(x)
print("Enter degree of polnomial to fit \n 2 for quadratic \t 3 for cubic")
n = int(input("Degree of polynomial: ")) 
A = np.zeros((n+1, n+1))
B = np.zeros(n+1)
a = np.zeros(n+1)
#-----------------------------
for row in range(n+1):
    for col in range(n+1):
        if row == 0 and col ==0:
            A[row, col] = m
            continue
        A[row,col] = np.sum(x**(row+col))
    B[row] = np.sum(x**row*y)
a = np.linalg.solve(A,B)
#---------------------------------
print('f(x) = \t %f'%a[0])
for i in range(1,n+1):
    print('\t %+f x^%d' %(a[i],i))
