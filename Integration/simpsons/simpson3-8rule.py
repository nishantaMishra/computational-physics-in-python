"""Integrating (sin(x)/x) from 0 to pi """

from math import sin, pi

f = lambda x: (sin(x)/x)

a = 0.0000000000000000000000001
b = pi/2
n = 12   #number of divisions, must be divisible by 3 fo simpson'sum 3/8 rule.

h = (b-a)/n 
sum = (f(a) + f(b))
for i in range(1, n, 3): # from 1 to n-2 in steps of 3
    sum += 3*(f(a +i*h) + f(a + (1+i)*h))
for i in range(3, n, 3):
    sum += 2*f(a +i*h)
integral = 3*h/8 * sum

print('The approx value of integral according to Simpson\'s 3/8 rule is %f' %integral )
