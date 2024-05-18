
"""Integrating (sin(x)/x) from 0 to pi """

from math import sin, pi
f = lambda x: (sin(x)/x)
a = 0.00000000000000000000000000000001
b = pi/2
n = 10   #number of divisions, must be even for simpson'sum 1/3 rule.
h = (b-a)/n 
sum = (f(a) + f(b))
for i in range(1, n, 2): # from 1 to n-2 in steps of 2, odd numbers
    sum += 4*f(a +i*h)
for i in range(2, n, 2): # from 2 to n-2 in steps of 2, even number
    sum += 2*f(a + i*h)
integral = h/3*sum
print('The value of inntegral according to Simpson\'sum 1/3 Rule is %f ' % integral)
#-------------
"""Above, starting exactly from zero 
will give "ZeroDivisionError: float division by zero"
for sinc function. Hence starting from a point close to 0
"""