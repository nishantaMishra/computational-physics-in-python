##############################################################
###     Plotting a Graph of Derivatives of function      ###
#############################################################
""" Visualising the derivatives by plotting their graph """ 

import numpy as np
import matplotlib.pyplot as plt
#-----------
def f(x):
    return 5*x**3 + 3*x**2 - 10*x + 2
#----------
h = 0.01
x = np.linspace(0,6,61)

# Central differences approximation
cd1f = (f(x+h)-f(x-h))/(2*h)
cd2f = (f(x+h)-2*f(x)+f(x-h))/h**2

# Plotting results
plt.plot(x,f(x),'-k', x,cd1f,'--b', x,cd2f,'-.r') # refer https://matplotlib.org/stable/gallery/color/named_colors.html
plt.title('Graph of Derivatives')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['f(x)','f \'(x)','f \'\'(x)'])
plt.grid()
plt.show()

