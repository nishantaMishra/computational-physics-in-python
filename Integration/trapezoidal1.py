
"""Integrating (sin(x)/x) from 0 to pi """

from math import sin, pi
f = lambda x: (sin(x)/x)
a = 0000000000000.1
b = pi/2
n = 500   #number of divisions, increase this number for accuracy.
h = (b-a)/n 
sum = 0.5*(f(a) + f(b))
for i in range(1,n): # from 1 to n-1, last number is not included
    sum += f(a + i*h)
integral = h*sum
print('Integral = %f' % integral)