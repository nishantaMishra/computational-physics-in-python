###################################################################
#####  Differentiation using Forward Difference Approximation ####
###################################################################

f = lambda x: x**3 + 3*x**2 -1
h = 0.01
x = 0.1
#----------------
fd1f = (f(x+h)- f(x))/h    #fd1f for forward first derivative of f
fd2f = (f(x+2*h) - 2*f(x+h) + f(x))/h**2
#--------------------
print('first derivative at %f is %f '%(x, fd1f))
print('second derivative at %f is %f '%(x, fd2f))