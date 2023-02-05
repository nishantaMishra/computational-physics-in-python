###############################################
#######      Gauss Seidel's Method       ######
###############################################

import numpy as np
a = np.array([[4, 1, 2, -1],
           [3, 6, -1, 2],
           [2, -1, 5, -3],
           [4, 1, -3, -8]],float)
b = np.array([2, -1, 3, 2], float)
(n,) = np.shape(b)
x = np.full(n, 1.0, float) # initial value of x is 1.0
xdiff = np.empty(n, float)
iterlimit = 100
tolerance = 1.0e-6

# iterations:
for iteration in range(iterlimit):
    for i in range(n):
        s = 0
        for j in range(n):
            if j != i:
                s += a[i, j]*x[j]
        xnew = -1/a[i,i] * (s - b[i])
        xdiff[i] = abs(xnew - x[i]) # corrected
        x[i] = xnew
    if(xdiff < tolerance).all():
        break

print('Number of iterations: %d '% (iteration+1))
print('The solution of the system:')
print(x)


