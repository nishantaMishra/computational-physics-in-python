#################################################
#####       Newton Raphson Function       ###### 
################################################
from numpy import *

x1 = float(input("Enter x1:"))
f =  lambda x: 2*x**2 - 5*x + 3 # refer https://www.w3schools.com/python/python_lambda.asp
df = lambda x: 4*x - 5

def NRF(f, df, x0, tol):
    """
    Defined a function for calculating root.
    This particular instance where function rturns to itself
    is called Recursion(A substitute of For loop).
    """
    print(x0)
    if abs(f(x0)) < tol:
        print('The value of root is', x0)
        return x0
        print("this", x0)
    else:
        return NRF(f, df,x0 - f(x0)/df(x0), tol)
        
NRF(f, df, x1, 0.0000001)

      
