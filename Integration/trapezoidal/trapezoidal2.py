###########################################
## Trapezoidal rule by defining function  ###
###########################################
import math

def trapezoidal(f, a, b, n):
    """
    the definite integral of function f from a to b using the Trapezoidal Rule.

    Parameters:
    f : function
        The function to integrate.
    a : float
        The start point of the interval.
    b : float
        The end point of the interval.
    n : int
        The number of sub-intervals.

    Returns:
    float
        The approximate value of the integral.
    """
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    
    for i in range(1, n):
        integral += f(a + i * h)
    
    integral *= h
    return integral


def f(x):
    return math.sin(x)
a = 0
b = 1
n = 20 
    
result = trapezoidal(f, a, b, n)
print(f"The approximate value of the integral is: {result}")
