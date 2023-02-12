# Find root of 2*x**2 - 5*x + 3 = 0 using bisection method
import sys

x1 = float(input('Enter value of x1: '))
x2 = float(input('Enter value of x2: '))
y1 = 2*x1**2 - 5*x1 + 3
y2 = 2*x2**2 - 5*x2 + 3

if y1*y2 < 0:
    print('The root is not within the given interval')
    sys.exit()
for bisection in range(1,101):
    xh = (x1 + x2)/2
    yh = 2*xh**2 - 5*xh + 3
    y1 = 2*x1**2 - 5*x1 + 3

    if abs(y1) < 1.0E-6:
        break
    elif y1*yh < 0: #if the root is in first half interval.
        x2 = xh      #then make x2 =xh
    else:
        x1 = xh
print('The root: %0.5f' %x1)
print('The number of bisections:%d ' %bisection)

	
