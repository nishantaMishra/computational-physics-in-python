#########################################################################
#################         Simpson's Rule Integrtion         ##################
########################################################################
def f(x):
    return 1/(1+x)
    
#------------------------------------------------------------------------    
def sim(f, a, b, n):   #in order: integrand, lower limit, upper limit, number of grid points(must be even for sympson's rule to work).
    """ define simpson method, a and b are the lower and upper limits of
    the interval, n is number of points, dx is the slice
        """
    integ = 0
    h = float((b - a) / n) #width of each interval

    for i in range(1,n-1,2):
        integ += f((a+(i-1)*h)) + 4*f((a+i*h)) + f((a+(i+1)*h))
        integral = h/3.0 * integ
        
        #LaTeX: \int_{a}^{b} f(x) dx = f(x_{i-1}) + 4f(x_i) + f(x_{i+1})
        
    
    # if number of points is even, then error araise
    if (n % 2) == 0:
      raise ValueError("n must be an odd integer.")
        

    return integral

integrate = sim(f,0,1,99) 
print('\nValue of integral from Simpson rule is\n',integrate)
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("## Second Part of the question ##\n")
integrate2 = sim(f,0,1,3)
integrate4 = sim(f,0,1,5)
integrate8 = sim(f,0,1,9)
print('Value of integral for N = 2 is\n',integrate2)
print('\nValue of integral for N = 4 is\n',integrate4)
print('\nValue of integral for N = 8 is\n',integrate8)





