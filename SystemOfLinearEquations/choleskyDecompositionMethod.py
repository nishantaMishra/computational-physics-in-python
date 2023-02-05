###################################################################
##############     Cholesky Decomposition Method    ##################
###################################################################

from math import sqrt
import scipy.linalg 
import numpy as np
import sys
from numpy.linalg import inv
#-------------------------------------------------------------------------------------------
def cholesky(A):
    """Defined a function to perform a Cholesky decomposition of A, which must 
    be a symmetric and positive definite matrix. The function
    returns the lower triangular matrix, L.
        LUX = B, UX = Y, A = LU    """
    n = len(A)
    # Create zero matrix for L
    L = [[0.0] * n for i in range(n)]

    # Perform the Cholesky decomposition
    for i in range(n):
        for k in range(i+1):
            tmp_sum = sum(L[i][j] * L[k][j] for j in range(k))
            
            if (i == k): # Diagonal elements
                # LaTeX: l_{kk} = \sqrt{ a_{kk} - \sum^{k-1}_{j=1} l^2_{kj}}
                L[i][k] = sqrt(A[i][i] - tmp_sum)
            else:
                # LaTeX: l_{ik} = \frac{1}{l_{kk}} \left( a_{ik} - \sum^{k-1}_{j=1} l_{ij} l_{kj} \right)
                L[i][k] = (1.0 / L[k][k] * (A[i][k] - tmp_sum))
    return L
#------------------------------------------------------------------------------------
A = np.array([[4, -1, 0, 0], [-1, 4, -1, 0], [0, -1, 4, -1], [0, 0, -1, 4]])
B = np.array([[1],[0], [0], [0]])
U = scipy.linalg.cholesky(A, lower=False)
L = cholesky(A)

#----------------------------------------------------------------------
#print(np.array(L))
#print ('The given matrix is \n',A)
#print ('\n The lower triangular matrix L is: \n \n',np.array(L))
#print('\n The upper triangular matrix U is: \n',U)
#------------------------------------------------------------------------
"""	next operation is LU	"""
LU = np.dot(L,U)
#print('\n LU matrix is \n', LU)
#-----------------------------------------------------------------------
#Augmented matrix LU_B = A_B
LU_B = np.concatenate((LU, B), axis = 1)
#print('\n Augmented matrix is \n', LU_B) 
#-------------------------------------------------------------------------
"""Now we solve this set of equations using
    The Gauss Elimination method."""
# Gauss elimination method 
n = int(4)
a = LU_B 
x = np.zeros(n)   # defined a one d matrix of variables.

# Solving LUX = B . This is Gauss elimination metthod.
for i in range(n):
    if a[i][i] == 0.0:   #if this happens. Program will end.
        sys.exit('Divide by zero detected!')   
        
    for j in range(i+1, n): #range(start, stop, steps) | range(start, stop)---default step is 1 | range(stop) ---default start is zero.
        ratio = a[j][i]/a[i][i]
        
        for k in range(n+1):
            a[j][k] = a[j][k] - ratio * a[i][k]

# Back Substitution
x[n-1] = a[n-1][n]/a[n-1][n-1] #square bracket because this is a matrix(array). last element is(assigned) 2d's last element 

for i in range(n-2,-1,-1): # range argument (start at n-2 run till 0 (before -1) , reduce by 1) thai is this loop goes in backward direction.
    x[i] = a[i][n] #a[i][n] is the last element of every row(horizontal) . 
    for j in range(i+1,n):   #this loop is for summation in the analytic formula.
        x[i] = x[i] - a[i][j]*x[j]
    x[i] = x[i]/a[i][i]

# Displaying solution
print('\nRequired solution is: ') 
for i in range(n):
    print('X%d = %0.4f' %(i,x[i]), end = '\n') #% चिह्न का तात्पर्य है पूर्णाङ्क %  के स्थान पर float मान मुद्रित कराओ पर मात्र 4 तक । \t means tab space. \n is for new line
"""S = np.dot(L,U) #this is the matrix A
print(S)    
print('inverse of A using Direct module\n',inv(S))  # Inverse of A"""
#A inverse is L inverse transpose times L inverse
Linv = inv(L)
#print('\n Inverse of L is:\n',Linv)

# Program to transpose a matrix using a nested loop
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]
# iterate through rows
for i in range(len(Linv)):
   # iterate through columns
   for j in range(len(Linv[0])):
       result[j][i] = Linv[i][j]
       
Lit = np.array(result)       
#print('\nL Inverse Transpose:\n', Lit)

Ainv = np.dot(Lit,Linv)
print('\nInverse of A is L inverse transpose times L inverse.\nUsing Cholesky Decomposition Method A inverse is\n\n',Ainv)
########
########
while true: #infinity loop 1
	user = input("Say, Very good: ")
	if (user == "Very good" or user ==  "Good" or user == "very good"):
		print("Thankyou!")
		break
	else:
		print("You must say that")
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
