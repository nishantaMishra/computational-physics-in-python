### Secant Method for finding roots of an Equation ###

def secant(fn,x1,x2,tol,imax):
    for iteration in range(imax):
        xnew = x2 - (x2-x1)/(fn(x2)-fn(x1))*fn(x2)
        if abs(xnew-x2) < tol: break  #convergence condition.
        else:
            x1 = x2
            x2 = xnew
    else:
        print("Warning: Maimum number of iteration reached! Enter different values of x1 and x2 or increase the number of iterations.")
    return xnew, iteration
    
#Now, Defining the problem    
f =  lambda x: 2*x**3 - 5*x**2 + 8*x + 3 # refer https://www.w3schools.com/python/python_lambda.asp
x1 = float(input("Enter x1:"))
x2 = float(input("Enter x2:"))

root,n = secant(f, x1, x2, 0.000001, 100)
print("Root is %f at %d iterations"%(root,n))
