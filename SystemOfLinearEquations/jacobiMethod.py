###################################################
#########    Jacobi's Method (Base code)    ########
###################################################
""" Jacobi's Method for solving the system
of linear equations """
from numpy import *

a = array([[4, 1, 2, -1],
           [3, 6, -1, 2],
           [2, -1, 5, -3],
           [4, 1, -3, -8]],float)

b = array([2, -1, 3, 2], float)

(n,) = shape(b)
x = full(n, 1.0, float) #full is function similar to zeroes.
xnew = empty(n, float) # created am empty matrix
iterlimit = 100
tolerance = 1.0e-6

# iterations:
for iteration in range(iterlimit):
    for i in range(n):
        s = 0
        for j in range(n):
            if j != i:
                s += a[i, j]*x[j]
        xnew[i] = -1/a[i,i] * (s - b[i])
    if (abs(xnew - x) < tolerance).all(): #convergence
        break
    else:
        x = copy(xnew) # a numpy module. Instead of reassigning it creates a copy. 

print('Number of iterations: %d '% (iteration+1))
print('The solution of the system using Jacobi\'s Method is:')
print(x)
