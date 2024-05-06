#######################################################################
##########       Curve Fitting Using SciPy Function        ##########
######################################################################

x = [0,1, 2, 3, 4, 5]
y = [2, 8, 14, 28, 39, 62]
#---------------------------------------
from scipy.optimize import curve_fit
def f(x, a0, a1, a2):
    """Defined Quadratic equation for
    quadratic curve fitting.
    """
    return a0 + a1*x + a2*x**2
#-----------------------------------------
a,b = curve_fit(f, x, y) 
print(a) #a array contains coefficients of f
#--------------------------------------------
#coefficients could be used to print the equation. 
from sympy import *
u = Symbol('x')
grY = a[2]*u**2 + a[1]*u + a[0]
print('This is the equation of fitted curve', grY)