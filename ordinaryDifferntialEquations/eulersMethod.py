################################################
#####        Euler's Method           #####
#############################################
""" Solve y' = xy over the domain [0,2]
given y(0)=1
"""
dy = lambda x,y: x*y 
x = 0
xn = 2
y = 1
h = 0.1
n = int((xn-x)/h)
for i in range(n):
    y = y + dy(x,y)*h
    x = x + h
    print(x,y)
