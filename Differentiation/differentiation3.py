###################################################################
#####     Backward Difference Approximation     ####
###################################################################

f = lambda x: x**3 + 3*x**2 -1
h = 0.01
x = 0.1
#----------------
bd1f = (f(x)-f(x-h))/h
bd2f = (f(x)-2*f(x-h)+f(x-2*h))/h**2
#--------------------
print('first derivative at %f is %f '%(x, bd1f))
print('second derivative at %f is %f '%(x, bd2f))
