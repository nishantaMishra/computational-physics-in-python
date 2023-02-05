##############################################################
#####       Four Order Runge-Kutta Method       #####
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
print('x \t\t y(Runge-Kutta O(4)) \t y(analytical)')
print('%f \t %f \t\t %f' %(x,y,f(x)))
#---------------------------
for i in range(1, n+1):
    K1 = h*dy(x,y)
    K2 = h*dy(x + h/2,y + K1/2)
    K3 = h*dy(x + h/2,y + K2/2)
    K4 = h*dy(x + h,y + K3)
    y = y + (K1 + 2*K2 + 2*K3 + K4)/6
    x = x + h
    print('%f \t %f \t\t %f' %(x,y,f(x)))

#moreover, here we can change the value of h an see 
#it's effect on accuracy of the solution. 