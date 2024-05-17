##############################################################################
##    Differntiation using Central Difference Approximation   ##
##############################################################################
"""Accuracy of this method is more than that of Forwar and Backward"""
f = lambda x: x**3 + 3*x**2 -1
h = 0.01
x = 0.1
#----------------
cd1f = (f(x+h)-f(x-h))/(2*h)
cd2f = (f(x+h)-2*f(x)+f(x-h))/h**2
#--------------------
print('first derivative at %f is %f '%(x, cd1f))
print('second derivative at %f is %f '%(x, cd2f))
