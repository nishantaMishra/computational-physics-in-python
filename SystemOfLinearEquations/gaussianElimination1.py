#####################################################
#####  Gaussian Elimination Method (base code)   ###### 
###################################################
from numpy import array, zeros
a = array([[2, 7, -1, 3, 1],
           [2, 0, 4, 1, 7],
           [6, 0, -3, 2, -1],
           [2, 1, 2, -1, 2],
           [3, 4, 0, -2, 1]],float)
           
b = array([5, 7, 2, 3, 4], float)
n = len(b)
x = zeros(n, float)

#Elimination
for k in range(n-1):
    for i in range(k+1, n):
        fctr = a[k, k] / a[i, k]
        b[i] = b[k] - fctr*b[i]
        for j in range(k, n):
            a[i, j] = a[k, j] - fctr*a[i, j]
        
#Back-substitution
x[n-1] = b[n-1] / a[n-1, n-1]
for i in range(n-2, -1, -1):
    terms = 0
    for j in range(i+1, n):
        terms += a[i, j]*x[j]
    x[i] = (b[i] - terms)/a[i, i]

print('The solution of the system:')
print(x)
