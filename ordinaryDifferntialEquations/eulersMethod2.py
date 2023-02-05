##############################################################
#####  Euler's Method (commparison with real solution)  #####
##############################################################
""" Solve y' = xy over the domain [0,2]
given y(0)=1
"""
from math import exp        #here to check accuracy of the solution 
f = lambda x: exp(x**2/2)    #we add a column of analytical solution as well.
#---------------------
dy = lambda x,y: x*y 
x = 0
xn = 2
y = 1
h = 0.1   
n = int((xn-x)/h)
#---------------------------
print('x \t\t  y \t\t y(analytical)')
print('%f \t %f \t %f' %(x,y,f(x)))
#---------------------------
for i in range(n):
    y = y + dy(x,y)*h
    x = x + h
    print('%f \t %f \t %f' %(x,y,f(x)))

#moreover, here we can change the value of h an see 
#it's effect on accuracy of the solution. 