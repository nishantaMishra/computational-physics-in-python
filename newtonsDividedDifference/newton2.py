#######################################################################
######   Newton divided difference interpolation (User Input)   ######
######################################################################
import numpy as np

n = int(input('Enter number of data points: '))
x = np.zeros((n))     #returns a array with zeroes. Refer https://numpy.org/doc/stable/reference/generated/numpy.zeros.html
print('Enter values of x:')
for i in range(n): 
        x[i] = float(input( 'x['+str(i)+']'))
#-------------------------------------------------------------------------------
y = np.zeros((n)) 
print('Enter values of y:')
for i in range(n): 
        y[i] = float(input( 'y['+str(i)+']'))

n = len(x) - 1
#----------------------------------------------------------------------
Dy = np.zeros((n+1, n+1)) 
Dy[:,0] = y 

# latex: Y_i^{j+1} = \frac{Y_i^{j} - Y_j^{j}}{(x_i - x_j)} #general formula for Newton's Divided Difference. 
for j in range(n):
    for i in range(j+1, n+1):
        Dy[i, j+1] = ((Dy[i,j] - Dy[j,j])/(x[i] - x[j]))
print("\n The Divide difference table is \n ", Dy)


xp = float(input('Enter the value of x where y has to be calculated: '))
yp = Dy[0,0] #y at point
for i in range(n):
    xprod = 1
    for j in range(i+1):
        xprod *= xp - x[j]
    yp += xprod*Dy[i+1, i+1]

print('For x= %.1f, the value of y is = %.1f' %(xp,yp))
