#### Method of False Position ####
# Regula Falsi method of finding roots of an algebraic equation
#x_new = x2 - \frac{(x2-x1)}{y2-y1} \times y2

def RegulaFalsi(fn, x1, x2, tol=0.001, ilimit=100): #defining a function called RegulaFalsi.
    y1 = fn(x1)
    y2 = fn(x2)
    xh = 0
    ifalsepos = 0 # Counter of the number of false positions.
    if y1 == 0: xh = x1
    elif y2 == 0: xh = x2
    elif y1*y2 > 0:
        print('No roots of the equation exist within the given interval.')
    else:
        for ifalsepos in range(1, ilimit+1):
            xh = x2 - (x2-x1)/(y2-y1)*y2
            yh = fn(xh)
            if abs(yh) < tol:
                break
            elif y1*yh < 0:
                x2 = xh
                y2 = yh
            else:
                x1 = xh
                y1 = yh
    return xh, ifalsepos   # Function returns two values. 


def y(x): return 2*x**2 - 5*x + 3
x1 = float(input('Enter the value of x1: '))
x2 = float(input('Enter the value of x2: '))


x,n = RegulaFalsi(y, x1, x2, 0.0000001)  #calling the function and assigning x to the first return value and n to the second return value.

print('The root:%f' %x)
print('The number of computed false position: %d' %n)

