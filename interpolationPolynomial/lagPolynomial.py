#####################################################################
#######   Get the Polynomial using Lagrange Interpolation   #########
####################################################################

#from sympy import Symbol
from sympy import *
import numpy as np
u = Symbol('u')
#-----------------------------------------------------------------------------
n = int(input('Enter number of data points: '))
x = np.zeros((n)) 
print('Enter values of x:')
for i in range(n): 
        x[i] = float(input( 'x['+str(i)+']'))
#-------------------------------------------------------------------------------
y = np.zeros((n)) 
print('Enter values of y:')
for i in range(n): 
        y[i] = float(input( 'y['+str(i)+']'))
#------------------------------------------------------------------------------------
#x = [0, 1, 2]
#y = [1, 3, 2]
P = [0, 1, 2, 3, 4, 5, 6, 7]
#P = list
O = 0
for i in range(n):
	pro = 1 
	for j in range(n):
		if i != j:
			P[i]=(u-x[j])/(x[i]-x[j])
			pro = pro*P[i]
			#LaTeX; P_i(x) = \prod_{j=1, j \neq i}^n \frac{x - x_j}{x_i - x_j}
	pro = pro*y[i]
	O = O+pro
	#print(pro)
#print(O)
#print(y)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
print('\nPolynomial according to lagrange interpolation is:\n', expand(O)) #expand is a module of sympy. could have also used print(simplify(O)) https://docs.sympy.org/latest/tutorial/simplification.html
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~")
	
	
	
	
	
	
