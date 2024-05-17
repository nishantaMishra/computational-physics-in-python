###################################################################
#####  Differentiation using Forward Difference Approximation ####
###################################################################

f = lambda x: x**3 + 3*x**2 -1
h = 0.01
x = 0.1
#----------------
first_forward_derivative = (f(x+h)- f(x))/h   
second_forward_derivative = (f(x+2*h) - 2*f(x+h) + f(x))/h**2
#--------------------
print('first derivative at %f is %f '%(x, first_forward_derivative))
print('second derivative at %f is %f '%(x, second_forward_derivative))
